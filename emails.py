#!/usr/bin/env python3
from email.message import EmailMessage
import os
import mimetypes

def generate_email(sender, recipient, subject, body, attachment):
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.setcontent(body)
    attachmentName = os.path.basename(attachment)
    mime_type,_ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split("/",1)
    with open(attachment, "rb") as attachmentFile:
        message.add_attachment(attachmentFile.read(), maintype=mime_type, subtype=mime_subtype, filename=attachmentName)
    return email
    
def send_email(email):
  mailServer = smtplib.SMTP("localhost")
  mailServer.send_message(email)
  mailServer.quit()
  