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

    $.ajax({
        url: verify_url,
        method: 'GET',
        data: {},
        success: function(data){
            var newCount
            if(data.verified){
                console.log("Verified!")
                newCount = verifyCount + 1
                this_.attr("data-verifies", newCount)
                $('#VerifyUnverify'+reportID).text('Unverify')
                $('#verifies_'+reportID).text(newCount)
            }else{
                console.log("Unverified!")
                newCount = verifyCount - 1
                this_.attr("data-verifies", newCount)
                $('#VerifyUnverify'+reportID).text('Verify')
                $('#verifies_'+reportID).text(newCount)
            }
        },
        error: function(e){
            console.log(e.message)
        }
    })
})
