from schoollife.Database import Database
from schoollife.Email import Email
from tkinter import *
import easygui


class Main:
    def __init__(self):
        self.datenbase = Database('data/benutzer-db.json')
        self.email = Email('reg.schoollife@gmail.com', 'LeanderLuka')

    def registration(self):
        while True:
            auswahlAnmeldung = easygui.buttonbox("Wilkommen bei Schoollife", "Schoollife", ["Anmelden", "Registrieren"])
            if auswahlAnmeldung == "Anmelden":
                anmeldedaten = easygui.multpasswordbox("Anmelden", "Schoollife", ["E-Mail", "Passwort"])
                user = self.datenbase.readUser(anmeldedaten[0])
                if (user is None):  # User nicht in DB gefunden
                    easygui.msgbox("User exestiert nicht")
                elif user["passwort"] != anmeldedaten[1]:  # Passwort stimmt nicht mit DB ueberein
                    easygui.msgbox("Falsches Passwort, haste gesoffen?")
                else:
                    easygui.msgbox("Anmeldung war erfolgreich")
                    return user
            elif auswahlAnmeldung == "Registrieren":
                registrierungsdaten = easygui.multenterbox("REGISTRIEREN", "SCHOOLLIFE",
                                                           ["Nachname", "Vorname", "E-mail Adresse", "Passwort",
                                                            "Passwort bestaetigen"])
                if registrierungsdaten[3] != registrierungsdaten[4]:
                    easygui.msgbox("Passwoerter stimmen nicht uebernrin")
                elif self.datenbase.readUser(registrierungsdaten[2]) is not None:
                    easygui.msgbox("Benutzer mit email exestiert schon!")
                else:
                    neuerUser = {
                        "nachname": registrierungsdaten[0],
                        "vorname": registrierungsdaten[1],
                        "email": registrierungsdaten[2],
                        "passwort": registrierungsdaten[3]
                    }
                    self.datenbase.saveUser(neuerUser)
                    self.email.send_registration_mail(registrierungsdaten[2])
                    easygui.msgbox("Benutzer wurde erfolgreich angelegt!")

    def testMenu(self, user):
        root = Tk()
        root.geometry("450x350")
        menu = Menu(root)

        subMenu = Menu(menu)
        menu.add_cascade(label="Schoollife", menu=subMenu)
        subMenu.add_command(label="Notenschnittrechner", command=self.do_nothing)
        subMenu.add_command(label="Do nothing", command=self.do_nothing)

        editMenu = Menu(menu)
        menu.add_cascade(label="Help", menu=editMenu)
        editMenu.add_command(label="Exit", command=self.exit)
        label = Label(root, text="Schoollife 0.3 - Hallo " + user["vorname"])
        label.pack()
        root.config(menu=menu)

    def exit(self):
        self.datenbase.saveDatabase()
        self.email.quit()
        exit(0)

    def do_nothing(self):
        print('doNothing')


if __name__ == "__main__":
    x = Main()
    user = x.registration()
    x.testMenu(user)
    mainloop()
