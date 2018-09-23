// Landing Page
function initMapLandingPage(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(
            function(pos){
                $('#userLat').text(parseFloat(pos.coords.latitude).toFixed(4))
                $('#userLng').text(parseFloat(pos.coords.longitude).toFixed(4))
                
                userCoordinates = {lat: pos.coords.latitude, lng: pos.coords.longitude}

                // Display Google Map with Marker
                var map = new google.maps.Map(document.getElementById('map'),{zoom: 15, center: {lat: userCoordinates.lat, lng: userCoordinates.lng}})
                var marker = new google.maps.Marker({
                    position: {lat: pos.coords.latitude, lng: pos.coords.longitude}, 
                    map: map,
                })

                // Geocoder
                url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
                geocoder_url = url + pos.coords.latitude + ',' + pos.coords.longitude + '&key=AIzaSyBLvHFeixDacvhmdX-L_0EoG4of6n0pM1A'
                fetch(geocoder_url).then(res => res.json()).then((out) => {
                    $('#userAddress').text(out.results[0].formatted_address)
                })

                var strictBounds = new google.maps.LatLngBounds(
                    new google.maps.LatLng(6.84056094066974, 121.8659057354746), 
                    new google.maps.LatLng(7.4457874389567, 122.42999710690287)
                );

                if(!strictBounds.contains(userCoordinates)){
                    $('#id_info').text('Your Current Location Is Out Of Bounds. This Site Can Only Notify Zamboanga City Responders.')
                }
            },
            function(error){
                if(error.code === 1){
                    alert("Unable to Detect Location!")
                }
            },
            {
                enableHighAccuracy: true,
                setTimeout: 5000,
            }
        )
    }else{
        alert("Cannot Detect Current Location! Make Sure You Have Allowed Location Access")
    }
}


// responder-signup
var map, marker;
function initMapForResponderSignUp(){
    map = new google.maps.Map(document.getElementById('map'),{zoom: 15, center: {lat: 6.9214, lng: 122.0790},})

    marker = new google.maps.Marker({
        position: {lat: 6.9214, lng: 122.0790},
        map: map,
    })

    google.maps.event.addListener(map, 'click', function(event) {
        placeMarker(event.latLng);
    });

    function placeMarker(location) {
        marker.setMap(null)
        marker = new google.maps.Marker({
            position: location, 
            map: map
        });

        $('#id_address').val('Geocoding Location, Please Wait...');
        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
        geocoder_url = url + marker.getPosition().lat() + ',' + marker.getPosition().lng() + '&key=AIzaSyBLvHFeixDacvhmdX-L_0EoG4of6n0pM1A'
        fetch(geocoder_url).then(res => res.json()).then((out) => {
            newAddress = out.results[0].formatted_address
            $('#id_address').val(newAddress);
        })

        newLat = marker.getPosition().lat()
        newLng = marker.getPosition().lng()

        $('#id_latitude').val(newLat);
        $('#id_longitude').val(newLng);
    }
}

// report-create
function initMapReportCreate(){
    var strictBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(6.84056094066974, 121.8659057354746), 
        new google.maps.LatLng(7.4457874389567, 122.42999710690287)
    );

    userCoordinates = {lat: userLat, lng: userLng}
    
    if(!strictBounds.contains(userCoordinates)){
        userCoordinates = new google.maps.LatLng(6.9214, 122.0790);
        $('#id_latitude').val(6.9214);
        $('#id_longitude').val(122.0790);
        $('#id_address').val('Veterans Ave, Zamboanga, Zamboanga del Sur, Philippines');
        $('#id_info').text('We Have Reset Your Location Because Your Current Location Is Out Of Bounds.')
        
        $('#userLat').val(6.9214);
        $('#userLng').val(122.0790);
        $('#userAddress').val('Veterans Ave, Zamboanga, Zamboanga del Sur, Philippines');
    }
    
    map = new google.maps.Map(document.getElementById('map'),{zoom: 15, center: userCoordinates,})

    marker = new google.maps.Marker({
        position: userCoordinates,
        map: map,
    })

    google.maps.event.addListener(map, 'click', function(event) {
        placeMarker(event.latLng);
    });

    google.maps.event.addListener(map, 'dragend', function() {
        if (strictBounds.contains(map.getCenter())) return;

        var c = map.getCenter(),
        x = c.lng(),
        y = c.lat(),
        maxX = strictBounds.getNorthEast().lng(),
        maxY = strictBounds.getNorthEast().lat(),
        minX = strictBounds.getSouthWest().lng(),
        minY = strictBounds.getSouthWest().lat();

        if (x < minX) x = minX;
        if (x > maxX) x = maxX;
        if (y < minY) y = minY;
        if (y > maxY) y = maxY;

        map.setCenter(new google.maps.LatLng(y, x));
    });

    function placeMarker(location) {
        if(!strictBounds.contains(location)){
            alert('Location Out Of Bounds')
        }else{
            marker.setMap(null)
            marker = new google.maps.Marker({
                position: location, 
                map: map
            });

            // Geocoder
            document.getElementById('userAddress').innerHTML = 'Geocoding Location, Please Wait...'
            url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
            geocoder_url = url + marker.getPosition().lat() + ',' + marker.getPosition().lng() + '&key=AIzaSyBLvHFeixDacvhmdX-L_0EoG4of6n0pM1A'
            fetch(geocoder_url).then(res => res.json()).then((out) => {
                newAddress = out.results[0].formatted_address
                document.getElementById('userAddress').innerHTML = newAddress
                document.getElementById('id_info').innerHTML = ''
            })

            newLat = marker.getPosition().lat()
            document.getElementById('userLat').innerHTML = newLat
            newLng = marker.getPosition().lng()
            document.getElementById('userLng').innerHTML = newLng
        }
    }
}

// report-detail-reporter
function initMapReportDetailReporter(){
    reportCoordinates = {lat: reportLat, lng: reportLng}
    var map = new google.maps.Map(document.getElementById('map'),{zoom: 18, center: reportCoordinates,})

    var marker = new google.maps.Marker({
        position: reportCoordinates,
        map: map,
    })
}

// report-detail-responder
function initMapReportDetailResponder(){
    reportCoordinates = {lat: reportLat, lng: reportLng}
    var map = new google.maps.Map(document.getElementById('map'),{zoom: 18, center: reportCoordinates,})

    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    directionsDisplay.setMap(map);
    directionsDisplay.setPanel(document.getElementById('directionsPanel'));

    directionsService.route({
        origin: {lat: userLat, lng: userLng},
        destination: {lat: reportLat, lng: reportLng},
        travelMode: 'DRIVING'
        }, 
        function(response, status) {
            if (status === 'OK') {
                directionsDisplay.setDirections(response);
            } else {
                window.alert('Directions request failed due to ' + status);
            }
        }
    );
}