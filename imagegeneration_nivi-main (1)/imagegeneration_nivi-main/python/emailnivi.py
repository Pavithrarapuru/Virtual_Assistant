import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(to_whom,subject,content):
    sender_mail="tnithin9640@gmail.com"
    sender_pass="bgeedzssjdyibkgt"
    reciever_mail=to_whom
    # subject="test email"
    # message="this is an email from python"

    try:
        msg=MIMEMultipart()
        msg['From']=sender_mail
        msg["To"] = reciever_mail
        msg["subject"]=subject
        msg.attach(MIMEText(content,'plain'))
        
        with smtplib.SMTP('smtp.gmail.com',587) as server:
            server.starttls()
            server.login(sender_mail,sender_pass)
            server.sendmail(sender_mail,reciever_mail,msg.as_string())
            print("email sent successfully")
    except Exception as e:
        print(e)