from django.conf import settings
from django.core.mail import EmailMessage, send_mail # Email

def send_reporter_welcome_email(instance):
	email_subject = "Welcome To Reportbook!"
	email_body = """
Dear %s,

Thank you for subscribing to REPORTBOOK.

You have have subscribed using this information:
Username: %s
Firstname: %s
Lastname: %s
Email: %s

Help us innovate our emergency reporting for the greater good.
We hope that with REPORTBOOK we could help you in your
life.

As a verification method your account is deactivated by 
default. To activate your account please reply to us an 
image of you holding any government issued identification 
card. Make sure that the image you will be sending is clear 
and did not undergo any image editing. 

We will be sending an email to, %s, after the verification process.

For more information, contact us at: capstonetechnopreneurship@gmail.com

Sincerly,
Reportbook
""" % (instance.username, instance.username, instance.first_name, instance.last_name, instance.email, instance.email,)
	recipients_list = (instance.email,)
	email_from = settings.EMAIL_HOST_USER
	# send_mail(email_subject, email_body, email_from, recipients_list)

	email = EmailMessage(
		subject = email_subject, body = email_body, from_email = email_from,
		to = recipients_list, reply_to = recipients_list
	)
	sent = email.send(fail_silently=False)
	return True

def send_responder_welcome_email(instance):
	email_subject = "Welcome To Reportbook!"
	email_body = """
Dear %s,

Thank you for subscribing to REPORTBOOK.

You have have subscribed using this information:
Username: %s
Email: %s
Phone: %s

Help us innovate our emergency reporting for the greater good.
We hope that with REPORTBOOK we could help you respond to an 
emergency and save lives.

For more information, contact us at: capstonetechnopreneurship@gmail.com

Sincerly,
Reportbook
""" % (instance.username, instance.username, instance.email, instance.responder.phone_number,)

	recipients_list = (instance.email,)
	email_from = settings.EMAIL_HOST_USER
	# send_mail(email_subject, email_body, email_from, recipients_list)

	email = EmailMessage(
		subject = email_subject, body = email_body, from_email = email_from,
		to = recipients_list, reply_to = recipients_list
	)
	sent = email.send(fail_silently=False)
	return True