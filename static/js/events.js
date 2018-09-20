// Responder profile view, verify-unverify event function (Responder Detail)
$('.btn-verify').click(function(e){
    var this_ = $(this)
    var report_id = this_.attr('data-reportID')
    $("#Column"+report_id).attr("hidden", "hidden")
})

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

// Verify toggle function (Site)
$('.btn-verify').click(function(e){
    e.preventDefault()
    var this_ = $(this)
    var verify_url  = this_.attr('data-href')
    var verifyCount = parseInt(this_.attr('data-verifies'))
    var reportID    = parseInt(this_.attr("data-reportID"))
    $.ajax({
        url: verify_url,
        method: 'GET',
        data: {},
        success: function(data){
            var newCount
            if(data.verified){
                newCount = verifyCount + 1
                this_.attr("data-verifies", newCount)
                $('#VerifyUnverify'+reportID).text('Unverify')
                $('#verifies_'+reportID).text(newCount)
            }else{
                newCount = verifyCount - 1
                this_.attr("data-verifies", newCount)
                $('#VerifyUnverify'+reportID).text('Verify')
                $('#verifies_'+reportID).text(newCount)
            }
        },
        error: function(error){
            console.log('Error ' + error)
        }
    })
})