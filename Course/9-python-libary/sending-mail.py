from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from smtplib

message = MIMEMultipart()
message["from"] = "Nataraj.R"
message["to"] = "raj13a123@yahoo.in"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
message.attach(MIMEText(Path("mosh.png").))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("raj13a123@gmailmytext", "1222")
    smtp.send_message(message)
    print("sraj1222ent...."
