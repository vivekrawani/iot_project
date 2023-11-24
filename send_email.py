
import smtplib
from email.message import EmailMessage
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = 'smart.alert.tg2@gmail.com'
    msg['from'] = user
    password = '**********'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
    print("Email Sent")

if __name__ == '__main__':
    email_to = '2021ugec015@nitjsr.ac.in'
    email_alert("Test Message Subject", "Some message", email_to)

