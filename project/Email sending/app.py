#import required modules
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#sever configuuration
smtp_server ="smtp.gmail.com"
smpt_port =587
sender_email="prathyushathatha@gmail.com"
passkey="paciebhawgphkzrg"
def singleEmailSend(to_email:str,subject:str,body:str):
    msg=MIMEMultipart()
    msg['To']=to_email
    msg['From']=sender_email
    msg['Subject']=subject
    msg.attach(MIMEText(body,'plain'))


    try:
        #start the server
        server=SMTP(smtp_server,smpt_port)
        #start server
        server.starttls()
        #login to server
        server.login(sender_email,passkey)
        #send email
        server.sendmail(from_addr=sender_email,to_addrs=to_email,msg=msg.as_string())
        server.quit()
        return f"Successfully email send to{to_email}"
    except Exception as e:
        return f"Failed To send email because:{e}"
#
to_email=input("enter Email address:")
subject=input("Enter email Subject:")
body=input("Enter email Body:")
#call single Email send
print(singleEmailSend(to_email,subject,body))
        
    