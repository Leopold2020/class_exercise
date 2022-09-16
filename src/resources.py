#Oskar Svedlund
#TEINF-20
#2022-09-15
#Class exercise


class Establishment:
    def __init__(self, name, agreement, employees : list) -> None:
        self.name = name
        self.agrement = agreement
        self.employees = employees

    def change_name(self):
        self.name = input(">> ")

    def hire_staff(self):
        pass

    def change_agrement(self):
        pass



class Resturant(Establishment):
    def __init__(self, name, agrement, employees: list, menu : list) -> None:
        super().__init__(name, agrement, employees)
        self.menu = menu

    def check_menu(self):
        return self.menu



    
class Shop(Establishment):

    def __init__(self, name, agrement, employees, inventory : list) -> None:
        super().__init__(name, agrement, employees)
        self.inventory = inventory

    def check_inventory(self):
        return self.inventory


    