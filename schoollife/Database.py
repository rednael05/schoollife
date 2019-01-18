import json


class Database:

    def __init__(self, filename):
        file = open(filename, "r").read()
        self.daten = json.loads(file)

    def speicherBenutzer(self, user):
        list = self.daten['user']
        list.extend(user)
        self.daten['user'] = list

    def leseBenutzer(self, email):
        for user in self.daten['user']:
            if user['email'] == email:
                return user

    def speichereDatenbank(self):
        schreiben = open("benutzer-db.json", "w")
        schreiben.write(json.dumps(self.daten))
