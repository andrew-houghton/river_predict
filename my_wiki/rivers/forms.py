from django.forms import ModelForm, ModelChoiceField, FloatField
from .models import Section, Gauge, River, Points
from markdownx.fields import MarkdownxFormField


class SectionForm(ModelForm):

    class Meta:
        model = Section
        fields = ['name', 'river', 'grade', 'description', 'gauge', 'minimum']
        myfield = MarkdownxFormField()

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        self.fields['gauge'].required = False
        self.fields['minimum'].required = False


class RiverForm(ModelForm):

    class Meta:
        model = River
        fields = ['name', 'description']


class PointForm(ModelForm):
    class Meta:
        model = Points
        exclude = []
