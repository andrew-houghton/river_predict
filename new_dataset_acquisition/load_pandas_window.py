import pandas
import numpy as np
import os
from multiprocessing import Pool
from tqdm import tqdm
steps_der_day = 96


pickle_path = '../new_dataset/Pickles/combined_csvs.pickle'
df = pandas.read_pickle(pickle_path, compression='bz2')
print('Finished loading')


print('Loading and creating rainfall data column.')
dateparse = lambda x: pandas.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
rain_df = pandas.read_csv(
    '../old_dataset/nymboida_rain.csv', parse_dates=[0], date_parser=dateparse)
print('Rainfall data loaded from csv.')


print('Merging rainfall and level data into one dataframe.')
full_df = pandas.merge(df, rain_df, how='left')


print('Interpolating missing rainfall data')
# assume rain fell at a constant rate over the whole time period
# only fill in gaps of up to one day
full_df['Rainfall'].fillna(
    method='bfill', inplace=True, limit=steps_der_day - 1)
# Adjust for 15 minute time period
full_df['Rainfall'] /= steps_der_day
full_df = full_df.round(3)

print('Creating new columns with history.')
# Column will have a list with the previous river levels
previous_levels = 700
previous_rainfalls = previous_levels

num_chunks = 100

csv_filename = '../new_dataset/nymboida_gaussian_{}steps.csv'.format(
    previous_levels)

# to make life easier
try:
    os.remove(csv_filename)
except OSError:
    pass

full_df.dropna(inplace=True)

del full_df['Date']
del full_df['Discharge']


def create_history_column(col_name, num_timesteps, input_df):
    # print('Creating column history for {} with {} time steps.'.format(
    #     col_name, num_timesteps))
    input_df = input_df.assign(**{col_name.lower() + '_' + str(i): input_df[
                               col_name].shift(i) for i in range(1, previous_levels + 1)})
    return input_df


def write_chunk_to_csv(small_df):
    small_df = create_history_column(
        'Rainfall', previous_rainfalls, small_df)
    small_df = create_history_column(
        'Level', previous_levels, small_df)
    small_df.to_csv(csv_filename, header=False, mode='a', index=False)

# write header row manually
with open(csv_filename, 'w') as f:
    col_list = ['Rainfall', 'Level', ] + \
        ['rainfall' + str(i) for i in range(1, previous_rainfalls + 1)] + \
        ['level' + str(i) for i in range(1, previous_levels + 1)]
    f.write(','.join(col_list))

# write in data
chunks = np.array_split(full_df, num_chunks)
with Pool(4) as p:
    for _ in tqdm(p.imap_unordered(write_chunk_to_csv, chunks), total=num_chunks, unit='chunk'):
        pass

