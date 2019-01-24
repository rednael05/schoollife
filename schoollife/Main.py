from schoollife.Database import Database
import easygui
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email = 'reg.schoollife@gmail.com'
password = 'LeanderLuka'
send_to_email = 'kepalletsplay@gmail.com'
subject = 'Schoollife Registration'
message = 'Wilkommen bei Schoollife, der zukunft der School '


msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

filename = os.path.basename("Email.json")
attachment = open("Email.json", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)


class Main:
    def __init__(self):
        self.datenbase = Database('benutzer-db.json')

    def anmeldung(self):

        while True:
            auswahlAnmeldung = easygui.buttonbox("Wilkommen bei Schoollife", "Schoollife", ["Anmelden", "Registrieren"])
            if auswahlAnmeldung == "Anmelden":
                anmeldedaten = easygui.multpasswordbox("Anmelden", "Schoollife", ["E-Mail", "Passwort"])
                user = self.datenbase.leseBenutzer(anmeldedaten[0])
                if (user is None):  # User nicht in DB gefunden
                    easygui.msgbox("User exestiert nicht")
                elif (user["passwort"] != anmeldedaten[1]):  # Passwort stimmt nicht mit DB ueberein
                    easygui.msgbox("Falsches Passwort, haste gesoffen?")
                else:
                    easygui.msgbox("Anmeldung war erfolgreich")
                    break
            elif auswahlAnmeldung == "Registrieren":
                registrierungsdaten = easygui.multenterbox("REGISTRIEREN", "SCHOOLLIFE",
                                                           ["Nachname", "Vorname", "E-mail Adresse", "Passwort",
                                                            "Passwort bestaetigen"])
                if registrierungsdaten[3] != registrierungsdaten[4]:
                    easygui.msgbox("Passwoerter stimmen nicht uebernrin")
                elif self.datenbase.leseBenutzer(registrierungsdaten[2]) is not None:
                    easygui.msgbox("Benutzer mit email exestiert schon!")
                else:
                    neuerUser = {
                        "nachname": registrierungsdaten[0],
                        "vorname": registrierungsdaten[1],
                        "email": registrierungsdaten[2],
                        "passwort": registrierungsdaten[3]
                    }
                    self.datenbase.speicherBenutzer(neuerUser)
                    easygui.msgbox("Benutzer wurde erfolgreich angelegt!")
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()

                    print "successvull sent an Email to: " + send_to_email

    def benutzerAnzeigen(self):
        easygui.msgbox("Schoollife 0.3")


    def beenden(self):
        self.datenbase.speichereDatenbank()


if __name__ == "__main__":
    x = Main()
    x.anmeldung()
    x.benutzerAnzeigen()
    x.beenden()
