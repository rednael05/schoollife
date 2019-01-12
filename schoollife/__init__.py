import easygui
import json

auswahl = ["ANMELDEN", "REGISTRIEREN"]
lesen = open("benutzer-db.json", "r")
benutzerdaten = json.load(lesen)

auswahlAnmeldung = easygui.buttonbox("WILKOMMEN BEI SCHOOLLIFE", "SCHOOLLIFE", auswahl)
if auswahlAnmeldung == "ANMELDEN":
    anmeldedaten = easygui.multenterbox("ANMELDEN", "SCHOOLLIFE", ["NAME", "PASSWORT"])
elif auswahlAnmeldung == "REGISTRIEREN":
    registrierungsdaten = easygui.multenterbox("REGISTRIEREN", "SCHOOLLIFE", ["NACHNAME", "VORNAME", "E-MAIL ADRESSE", "PASSWORT", "PASSWORT BESTÄTIGEN"])
    if registrierungsdaten[3] != registrierungsdaten[4]:
        easygui.msgbox("PASWÖRTER STIMMEN NICHT ÜBEREIN")
    else:
        jsonDaten = {
            "nachname":registrierungsdaten[0],
            "vorname":registrierungsdaten[1],
            "email":registrierungsdaten[2],
            "passwort":registrierungsdaten[3]
        }
        schreiben = open("benutzer-db.json", "w")
        schreiben.write(json.dumps(benutzerdaten))
