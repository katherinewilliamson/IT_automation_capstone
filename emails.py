#!/usr/bin/env python3
from email.message import EmailMessage
import os
import mimetypes
import smtplib


def generate_email(sender, recipient, subject, body, attachment=None):
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(body)
    if attachment:
        attachmentName = os.path.basename(attachment)
        mime_type,_ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split("/",1)
        with open(attachment, "rb") as attachmentFile:
            email.add_attachment(attachmentFile.read(), maintype=mime_type, subtype=mime_subtype, filename=attachmentName)
    return email
    

def send_email(email):
    mailServer = smtplib.SMTP("localhost")
    mailServer.send_message(email)
    mailServer.quit()

