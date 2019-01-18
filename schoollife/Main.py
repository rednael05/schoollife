from schoollife.Database import Database
import easygui


class Main:
    def __init__(self):
        self.datenbase = Database('benutzer-db.json')

    def anmeldung(self):
        anmeldungAktiv = True

        while anmeldungAktiv:
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
                    break
            elif auswahlAnmeldung == "REGISTRIEREN":
                registrierungsdaten = easygui.multenterbox("REGISTRIEREN", "SCHOOLLIFE",
                                                           ["NACHNAME", "VORNAME", "E-MAIL ADRESSE", "PASSWORT",
                                                            "PASSWORT BESTÄTIGEN"])
                if registrierungsdaten[3] != registrierungsdaten[4]:
                    easygui.msgbox("PASWÖRTER STIMMEN NICHT ÜBEREIN")
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

    def benutzerAnzeigen(self):
        easygui.msgbox("Hier müsst ihr weiter machen!")

    def beenden(self):
        self.datenbase.speichereDatenbank()


if __name__ == "__main__":
    x = Main()
    x.anmeldung()
    x.benutzerAnzeigen()
    x.beenden()
