from schoollife.Database import Database
from schoollife.Email import Email
from tkinter import *
import easygui
import random



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
                    if user["freigeschaltet"]=="false":
                       code = easygui.passwordbox("Bitte Accoount freischalten",["Bestaetigungscode:"] )
                       print("code: "+code+" random: "+user["random"])
                       if code == user["random"]:
                            user["freigeschaltet"] = "true"
                            easygui.msgbox("Anmeldung war erfolgreich")
                            self.datenbase.saveDatabase()

                       else:
                        easygui.msgbox("Falscher Bestätigungscode")
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
                code = str(random.randint(100000, 999999))
                neuerUser = {
                    "nachname": registrierungsdaten[0],
                    "vorname": registrierungsdaten[1],
                    "email": registrierungsdaten[2],
                    "passwort": registrierungsdaten[3],
                    "random": code,
                    "freigeschaltet": "false"
                }

                self.datenbase.saveUser(neuerUser)
                self.email.send_registration_mail(registrierungsdaten[2],code)
                self.datenbase.saveDatabase()
                easygui.msgbox("Benutzer wurde erfolgreich angelegt!")

    def testMenu(self, user):
        self.root = Tk()
        self.root.geometry("450x350")
        menu = Menu(self.root)

        subMenu = Menu(menu)
        menu.add_cascade(label="Schoollife", menu=subMenu)
        subMenu.add_command(label="Notenschnittrechner", command=self.do_nothing)
        subMenu.add_command(label="Do nothing", command=self.do_nothing)

        editMenu = Menu(menu)
        menu.add_cascade(label="Help", menu=editMenu)
        editMenu.add_command(label="Exit", command=self.exit)
        label = Label(self.root, text="Schoollife 0.3 - Hallo " + user["vorname"])
        label.pack()
        self.root.config(menu=menu)

    def exit(self):
        self.datenbase.saveDatabase()
        self.email.quit()
        exit(0)



    def do_nothing(self):


        TopFrame = Frame()
        TopFrame.pack()

        Label_1 = Label(TopFrame, text="Note_1")
        Entry_1 = Entry(TopFrame)


        Label_1.pack( )
        Entry_1.grid(row=0 , column=1)


if __name__ == "__main__":
    x = Main()
    user = x.registration()
    x.testMenu(user)
    mainloop()
