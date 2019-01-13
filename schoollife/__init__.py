import random
import easygui
import json

print "Hello World"
auswahl = ["Anmelden", "Registrieren", "Abbruch"]
loop = 0
regdate = easygui.multenterbox("Bitte Daten Eingeben", "Schoollife", ["Gesamter Name", "Username", "Email Adresse", "Passwort", "Passwort wiederholen"])

read_file = open("benutzer-db.json")
benutzerdaten = json.load(read_file)
a2 = ["Abmelden", "Spielen"]
a1 = easygui.buttonbox("Was wollen sie machen", "Schoollife", a2)

a3 = ["Was ratet Spieler 1", "Was ratet Spieler 2"]
while loop < 1:

    loop = 0
    auswahlAnmeldung = easygui.buttonbox("Wilkommen","School life", auswahl)
    if auswahlAnmeldung == "Anmelden":
        adaten =easygui.multenterbox("Bitte Daten eingeben", "Schoollife.anmelden", ["Username", "Passwort"])
        if adaten[0] == benutzerdaten["Username"] and adaten[1] == benutzerdaten["Passwort"]:
            easygui.msgbox("Wilkommen"+" "+benutzerdaten["Username"])
            a1
        if a1[1] == "Abmelden":
            print "ok"
        elif a1[2] == "Spielen":
            easygui.multenterbox("Lass uns Zahlen raten spielen", "Schoollife", a3)

    else:
            easygui.msgbox("Falscher name oder Passwort")
    if auswahlAnmeldung == "Registrieren":
        regdate
        easygui.msgbox("Passwort ist nicht gleich")
    else:
                benutzerdaten = open("benutzer-db.json", "w")
                jsonDaten = {
                    "Voll. Name": regdate[0],
                    "Username": regdate[1],
                    "E-mail": regdate[2],
                    "Passwort": regdate[3]
                }
                benutzerdaten.write(json.dumps(jsonDaten))
                loop + 1
    if auswahlAnmeldung == "Abbruch":
                antwort = easygui.buttonbox("Wirklich abbrechen?", "Schoollife", ["Ja", "Nein"])
                if  antwort[1] == "Ja" :
                    print "ok" and loop + 1
                elif antwort[2] == "Nein":
                    print "ok"




