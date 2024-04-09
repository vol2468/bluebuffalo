import smtplib
from email.message import EmailMessage

from flask import redirect, url_for


def email_alert(subject, body, to):

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "bluebuffalo54321@gmail.com"
    msg['from'] = user
    password = "chyf iekq vtwy vsbh"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

    return True

    