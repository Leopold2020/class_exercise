#Oskar Svedlund
#TEINF-20
#2022-09-28
#heros-and-villans





class Hero:
    def __init__(self, name: str, seceret_identity: str, weakness: str, \
        catch_phrase: str, exposed: bool, rivals = []):
        self.name = name
        self.seceret_identity = seceret_identity
        self.weakness = weakness
        self.catch_phrase = catch_phrase
        self.exposed = exposed
        self.rivals = rivals

    def say_catch_phrase(self):
        return self.catch_phrase

    def expose(self):
        return True

    def get_identity(self):
        self.exposed = False
        self.seceret_identity = input(">>")


class Villan:
    def __init__(self, name: str, seceret_identity: str, hideout: str, seceret_plan: str, \
        evil_speech: str, henchmen: list, nemesis: str):
        self.name = name
        self.seceret_identity = seceret_identity
        self.hideout = hideout
        self.seceret_plan = seceret_plan
        self.evil_speech = evil_speech
        self.henchmen = henchmen
        self.nemesis = nemesis

    def get_identity(self):
        self.seceret_identity = input("")

    def reveal_plan(self):
        return self.seceret_plan
    
    


class Henchmen:
    def __init__(self, name: str, works_for: str, salary: int, role: str):
        self.name = name
        self.works_for = works_for
        self.salary = salary
        self.role = role