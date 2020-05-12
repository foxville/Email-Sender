import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'enter your name'
email['to'] = 'recipient\'s email'
email['subject'] = 'enter the subject'

email.set_content(html.substitute({'name':'enter any name'}), 'html') # the contents of the letter are in the attached index.html


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: # settings depend on your mail provider
	smtp.ehlo()
	smtp.starttls()
	smtp.login('your email','your email password') # be warned, using Google account you need to enable "Allow less secure apps" at https://myaccount.google.com/lesssecureapps
	smtp.send_message(email)
	print('Done!')