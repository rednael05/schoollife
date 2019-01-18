from schoollife.Database import Database
import easygui


class Main:
    def __init__(self):
        self.datenbase = Database('benutzer-db.json')

    # Two methods:
    def show(self):
        auswahlAnmeldung = easygui.buttonbox("WILKOMMEN BEI SCHOOLLIFE", "SCHOOLLIFE", ["ANMELDEN", "REGISTRIEREN"])
        if auswahlAnmeldung == "ANMELDEN":
            anmeldedaten = easygui.multenterbox("ANMELDEN", "SCHOOLLIFE", ["NAME", "PASSWORT"])
            user = self.datenbase.leseBenutzer(anmeldedaten[0])
            if (user is None):  # User nicht in DB gefunden
                easygui.msgbox("User exestiert nicht")
            elif (user["passwort"] != anmeldedaten[1]):  # Passwort stimmt nicht mit DB überein
                easygui.msgbox("Falsches Passwort")
            else:
                easygui.msgbox("Anmeldung war erfolgreich")
        elif auswahlAnmeldung == "REGISTRIEREN":
            registrierungsdaten = easygui.multenterbox("REGISTRIEREN", "SCHOOLLIFE",
                                                       ["NACHNAME", "VORNAME", "E-MAIL ADRESSE", "PASSWORT",
                                                        "PASSWORT BESTÄTIGEN"])
            if registrierungsdaten[3] != registrierungsdaten[4]:
                easygui.msgbox("PASWÖRTER STIMMEN NICHT ÜBEREIN")
            elif self.datenbase.leseBenutzer(registrierungsdaten[2]):
                easygui.msgbox("Benutzer mit email exestiert schon!")
            else:
                neuerUser = {
                    "nachname": registrierungsdaten[0],
                    "vorname": registrierungsdaten[1],
                    "email": registrierungsdaten[2],
                    "passwort": registrierungsdaten[3]
                }
            self.datenbase.leseBenutzer(neuerUser)
            easygui.msgbox("Benutzer wurde erfolgreich angelegt!")
        self.datenbase.speichereDatenbank()

if __name__ == "__main__":
    x = Main()
x.show()
