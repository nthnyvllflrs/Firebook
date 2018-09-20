// Retrieve CSRF Token Function (Timeline)
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Calculate and Update User Reporter Location (Timeline)
function calculateLocation(){
	navigator.geolocation.getCurrentPosition(
	    function(result){
	        var myLat = result.coords.latitude
	        var myLng = result.coords.longitude

	        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
	        $.ajax({
	            url: url + myLat + ',' + myLng + '&key=AIzaSyBLvHFeixDacvhmdX-L_0EoG4of6n0pM1A',
	            success: function(data){
	                var myAddress = data.results[0].formatted_address
	                data = {
	                    'csrfmiddlewaretoken': getCookie('csrftoken'),
	                    'latitude': myLat,
	                    'longitude': myLng,
	                    'address': myAddress,
	                }

	                $.ajax({
	                    url: urlLocation,
	                    type: 'POST',
	                    data: data,
	                    error: function(e){
	                        console.log(e)
	                    }
	                })
	            }
	        })
	    },
	    function(error){
	        console.log(error.code)
	    },
	    {
	        enableHighAccuracy: true,
	        setTimeout: 3000,
	    }
	)
}

// Set new location and coordinates function (Report Creation)
function setLocation(){
    $('#id_latitude').prop('readonly', false)
    $('#id_longitude').prop('readonly', false)
    $('#id_address').prop('readonly', false)

    $('#id_latitude').val(newLat);
    $('#id_longitude').val(newLng);
    $('#id_address').val(newAddress);

    $('#id_latitude').prop('readonly', true)
    $('#id_longitude').prop('readonly', true)
    $('#id_address').prop('readonly', true)
}

// Timeline Long Polling Function (Timeline)
function timelineLongPolling(){
    $("#timelineView").load(urlTimeline);
}

// Notification Long Polling (Notification) ~
function notificationLongPolling(){
	$("#notificationView").load(urlNotification);
}