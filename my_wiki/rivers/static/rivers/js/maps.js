var map;
var startMarker;
var endMarker;

function placeEnd() {
    // if any previous marker exists, let's first remove it from the map
    if (endMarker) {
        endMarker.setMap(null);
    }
    // create the marker
    endMarker = new google.maps.Marker({
        position: map.getCenter(),
        label: 'Take out',
        map: map,
        draggable: true,
    });

    fillMarkerForm(endMarker,'id_form-0-');
    google.maps.event.addListener(endMarker, 'dragend', function() {
        fillMarkerForm(endMarker,'id_form-0-');
    });
}

function placeStart(){
    // if any previous marker exists, let's first remove it from the map
    if (startMarker) {
        startMarker.setMap(null);
    }
    // create the marker
    startMarker = new google.maps.Marker({
        position: map.getCenter(),
        label: 'Put in',
        map: map,
        draggable: true,
    });

    fillMarkerForm(startMarker,'id_form-1-');
    google.maps.event.addListener(startMarker, 'dragend', function() {
        fillMarkerForm(startMarker,'id_form-1-');
    });
}

function initialize() {
    var originLocation = new google.maps.LatLng(-33.865143, 151.209900); // Sydney
    var mapOptions = {
        zoom: 8,
        center: originLocation
    }
    map = new google.maps.Map(document.getElementById("map"), mapOptions);

    // Add controls to the map
    var buttonPutIn = document.createElement('div');
    var controlArgs = {
        'Take out': 'placeEnd',
        'Put in': 'placeStart',
    }
    var centerControl = new CenterControl(buttonPutIn, controlArgs);
    buttonPutIn.index = 1;
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(buttonPutIn);

}

google.maps.event.addDomListener(window, 'load', initialize);


function submitForm(){
    
    document.getElementById("formgrid").submit();
}

function fillMarkerForm(marker,id){
    if (marker){
        pos = marker.getPosition()
        document.getElementById(id+"latitude").value = pos.lat().toFixed(6)
        document.getElementById(id+"longditude").value = pos.lng().toFixed(6)
    }
}