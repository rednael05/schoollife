from schoollife.Database import Database
from schoollife.Email import Email
from Tkinter import *
import easygui


class Main:
    def __init__(self):
        self.datenbase = Database('data/benutzer-db.json')
        self.email = Email('benutzer-db.json')

    def registration(self):
        while True:
            auswahlAnmeldung = easygui.buttonbox("Wilkommen bei Schoollife", "Schoollife", ["Anmelden", "Registrieren"])
            if auswahlAnmeldung == "Anmelden":
                anmeldedaten = easygui.multpasswordbox("Anmelden", "Schoollife", ["E-Mail", "Passwort"])
                user = self.datenbase.readUser(anmeldedaten[0])
                if (user is None):  # User nicht in DB gefunden
                    easygui.msgbox("User exestiert nicht")
                elif (user["passwort"] != anmeldedaten[1]):  # Passwort stimmt nicht mit DB ueberein
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

    def main_window(user):
        root = Tk()

        menu = Menu(root)
        root.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="Schoollife", menu=subMenu)
        subMenu.add_command(label="Notenschnittrechner", command=doNothing)
        subMenu.add_command(label="Exit", command=doNothing)

        editMenu = Menu(menu)
        menu.add_cascade(label="File:", menu=editMenu)
        editMenu.add_command(label="Undo", command=doNothing)
        label = Label(root, text="Schoollife 0.3", fg="WHITE", bg="BLACK")
        label.pack(fill=X, side="top")

        root.mainloop()

    def exit(self):
        self.datenbase.saveDatabase()
        self.email.quit()
        exit(0)


if __name__ == "__main__":
    x = Main()
    user = x.registration()
    x.main_window(user)
    x.exit()
