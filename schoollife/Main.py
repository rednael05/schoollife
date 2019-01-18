from schoollife.Database import Database


class Main:
    def __init__(self):
        self.datenbase = Database('benutzer-db.json')

    # Two methods:
    def show(self):
        self.datenbase.speicherBenutzer({"test": "value"})
        self.datenbase.leseBenutzer()
        self.datenbase.speichereDatenbank()


if __name__ == "__main__":
    x = Main()
    x.show()
