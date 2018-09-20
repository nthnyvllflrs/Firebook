// Notification view details event function (Notification)
$('.view-detail').click(function(e){
    console.log("DEtail")
	e.preventDefault()
	var this_ = $(this)
	var notification_id = this_.attr('data-notification')
	var notification_url = this_.attr('data-url')
	var notification_redirect = this_.attr('data-redirect')

	$.ajax({
		url: notification_url,
		method: 'GET',
		data: {},
		success: function(data){
			window.location.href = notification_redirect
		},
		error: function(error){
			console.log(error)
		}
	})
})

// Notification close event function (Notification)
$('.notif-close').click(function(e){
    console.log("CLose")
	e.preventDefault()
	var this_ = $(this)
	var notification_id  = this_.attr('data-notification')
	var notification_url = this_.attr('data-url')

	$.ajax({
		url: notification_url,
		method: 'GET',
		data: {},
		success: function(data){},
		error: function(error){}
	})
})