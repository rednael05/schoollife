import json


class Database:

    def __init__(self, filename):
        file = open(filename, "r").read()
        self.daten = json.loads(file)

    def speicherBenutzer(self, user):
        print(self.daten)
        list = self.daten['user']
        list.extend(user)
        self.daten['user'] = list

    def leseBenutzer(self, email):
        print(self.daten)

    def speichereDatenbank(self):
        schreiben = open("benutzer-db.json", "w")
        schreiben.write(json.dumps(self.daten))
