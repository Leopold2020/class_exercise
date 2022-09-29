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

    def recruit_hencmen(self, new_hench: list):
        self.new_hench = new_hench
        # name = input("Henchmen name\n>> ")
        # salary = int(input("Salary\n>> "))
        # role = input("Role\n>> ")

        self.henchmen.append(Henchmen(self.new_hench))
    
    


class Henchmen:
    def __init__(self, name: str, works_for: str, salary: int, role: str):
        self.name = name
        self.works_for = works_for
        self.salary = salary
        self.role = role


#----------------------------------------------------------------------------------------------------------








def make_hero():
    heroname = input("Hero name\n>> ")
    heroidentity = input("Seceret identity\n>> ")
    heroweakness = input("Weakness\n>> ")
    herochatchphrase = input("Catch phrase\n>> ")


    return Hero(heroname, heroidentity, heroweakness, herochatchphrase, False, None)

def make_villan():
    villanname = input("Villan name\n>> ")
    villanidentity = input("Seceret identity\n>> ")
    villanhideout = input("Seceret hideout\n>> ")
    villanplan = input("")


    return Villan(villanname,)


def main():
    choice1 = input("What do you whant to do?\n>> ")

    if choice1 == "1":

        newperson = input("New person\n1. Hero\n2. Villan>>")

        if newperson == "1":
            make_hero()


        elif newperson == "2":
            villanname = input("Villan name\n>> ")

    


if __name__ == "__main__":
    main()