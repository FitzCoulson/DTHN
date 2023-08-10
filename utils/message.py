import smtplib
from email.mime.text import MIMEText

def send_message(content):
    mail_host = 'smtp.qq.com'
    mail_user = '1289391408'
    mail_pass = 'mmuqhipphgqigbfe'
    sender = '1289391408@qq.com'
    receivers = ['1289391408@qq.com']
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = 'Experiment Result'
    message['From'] = sender
    message['To'] = receivers[0]

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print('error', e)
