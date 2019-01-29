import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self, login_mail):
        self.email_from = login_mail
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(login_mail, 'LeanderLuka')

    def send_registration_mail(self, to_mail):
        msg = MIMEMultipart()
        msg['From'] = self.email_from
        msg['Subject'] = 'Schoollife Registration'
        msg.attach(MIMEText('Wilkommen bei Schoollife, der zukunft der Schule ', 'plain'))
        text = msg.as_string()
        self.server.sendmail(self.email_from, to_mail, text)

    def quit(self):
        self.server.quit()
