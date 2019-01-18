from schoollife.Database import Database


class Main:
    def __init__(self):
        self.datenbase = Database('benutzer-db.json')

    # Two methods:
    def show(self):
        user = self.datenbase.leseBenutzer("otto@test.de")
        print(user['name'])
        self.datenbase.speicherBenutzer({"name": "Leander",
                                         "email": "leander@bonsch.de",
                                         "pass": "test"})
        self.datenbase.speichereDatenbank()


if __name__ == "__main__":
    x = Main()
    x.show()
