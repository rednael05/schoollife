import json


class Database:

    def __init__(self, filename):
        file = open(filename, "r").read()
        self.daten = json.loads(file)
        self.db_file = filename

    def saveUser(self, user):
        self.daten['user'].append(user)
        schreiben = open(self.db_file, "w")
        schreiben.write(json.dumps(self.daten))

    def readUser(self, email):
        for user in self.daten['user']:
            if user['email'] == email:
                return user

    def saveDatabase(self):
        schreiben = open(self.db_file, "w")
        schreiben.write(json.dumps(self.daten))
