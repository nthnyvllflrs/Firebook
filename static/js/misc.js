// user-change-password
$("input").addClass( "form-control" )
$("#id_old_password").attr("placeholder", "Old Password")
$("#id_new_password1").attr("placeholder", "New Password")
$("#id_new_password2").attr("placeholder", "Confirm New Password")

// report-create
$('#id_latitude').prop('readonly', true)
$('#id_longitude').prop('readonly', true)
$('#id_address').prop('readonly', true)