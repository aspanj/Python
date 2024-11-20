class Tier:
    def __init__(self, name: str, alter: int):
        self.name = name
        self.alter = alter
    
    def gib_info(self):
        pass

    def gib_laut(self):
        pass

class Hund(Tier):
    def gib_info(self):
        print(f"Name: {self.name}, Alter: {self.alter} Jahre, Art: Hund")

    def gib_laut(self):
        print("Wuff!")


class Vogel(Tier):
    def gib_info(self):
        print(f"Name: {self.name}, Alter: {self.alter} Jahre, Art: Vogel")

    def gib_laut(self):
        print("Zwitscher!")

class Löwe(Tier):
    def gib_info(self):
        print(f"Name: {self.name}, Alter: {self.alter} Jahre, Art: Löwe")
    
    def gib_laut(self):
        print("Roar")


hund = Hund("Bello", 5)
vogel = Vogel("Tweety", 2)
loewe = Löwe("Simba", 7)


hund.gib_laut()

