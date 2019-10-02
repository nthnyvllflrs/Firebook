// Responder profile view, remove fire fighter function (Responder Detail)
$('.btn-remove').click(function(e){
    var this_ = $(this)
    var fighter_id = this_.attr('data-fighterID')
    var remove_url = this_.attr('data-href')

    $("#FighterColumn"+fighter_id).attr("hidden", "hidden")

    $.ajax({
        url: remove_url,
        method: 'GET',
        data: {},
        success: function(data){
            window.location.href=window.location.href
        },
        error: function(data){
            console.log(data)
        }
    })
})

// Responder profile view, verify-unverify event function (Responder Detail)
$('.btn-verify').click(function(e){
    var this_ = $(this)
    var report_id = this_.attr('data-reportID')
    $("#Column"+report_id).attr("hidden", "hidden")
})

// Verify toggle function (Site)
$('.btn-verify').click(function(e){
    e.preventDefault()
    var this_ = $(this)
    var verify_url  = this_.attr('data-href')
    var verifyCount = parseInt(this_.attr('data-verifies'))
    var reportID    = parseInt(this_.attr("data-reportID"))

    $("#verify_btn_"+reportID).attr("disabled", true) 

    $.ajax({
        url: verify_url,
        method: 'GET',
        data: {},
        success: function(data){
            var newCount
            if(data.verified){
                newCount = verifyCount + 1
                this_.attr("data-verifies", newCount)
                // $('#VerifyUnverify'+reportID).text('Unverify')
                $('#verifies_'+reportID).text(newCount)

                $("#verify_btn_"+reportID).addClass("btn-primary")
                $("#verify_btn_"+reportID).removeClass("btn-outline-primary")
            }else{
                newCount = verifyCount - 1
                this_.attr("data-verifies", newCount)
                // $('#VerifyUnverify'+reportID).text('Verify')
                $('#verifies_'+reportID).text(newCount)

                $("#verify_btn_"+reportID).addClass("btn-outline-primary")
                $("#verify_btn_"+reportID).removeClass("btn-primary")
            }
            $("#verify_btn_"+reportID).attr("disabled", false) 
        },
        error: function(e){
            console.log(e.message)
        }
    })
})

// Status toggle function (Site)
$('.btn-status').click(function(e){
    e.preventDefault()
    var this_ = $(this)
    var status_url  = this_.attr('data-href')
    var reportID    = parseInt(this_.attr("data-reportID"))

    $.ajax({
        url: status_url,
        method: 'GET',
        data: {},
        success: function(data){
            $('#status_'+reportID).text("Cleared")
            $(".btn-status").attr("hidden", "hidden")
        },
        error: function(e){
            console.log(e.message)
        }
    })
})

// Respond toggle function (Site)
$('.btn-respond').click(function(e){
    e.preventDefault()
    var this_ = $(this)
    var respond_url  = this_.attr('data-href')
    var reportID    = parseInt(this_.attr("data-reportID"))

    $.ajax({
        url: respond_url,
        method: 'GET',
        data: {},
        success: function(data){
            console.log(data)
            $(".btn-respond").attr("hidden", "hidden")
            window.location.href=window.location.href
        },
        error: function(e){
            console.log(e.message)
        }
    })
})