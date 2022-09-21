#Oskar Svedlund
#TEINF-20
#2022-09-15
#Class exercise


class Establishment:
    def __init__(self, name, agreement, employees : list, income : int, expenditure : int) -> None:
        self.name = name
        self.agrement = agreement
        self.employees = employees
        self.income = income
        self.expenditure = expenditure

    def change_name(self):
        self.name = input(">> ")

    def hire_staff(self):
        self.employees.append(input("Name the new employee\n>> "))

    def change_agrement(self):
        self.agrement = input("New agreement\n>> ")

    def change_income(self, new_income):
        self.income = new_income

    def change_expenditure(self, new_expenditure):
        self.expenditure = new_expenditure


class Resturant(Establishment):
    def __init__(self, name, agrement, employees: list, income : int, expenditure : int, menu : list) -> None:
        super().__init__(name, agrement, employees, income, expenditure)
        self.menu = menu

    def check_menu(self):
        return self.menu


class Shop(Establishment):
    def __init__(self, name, agrement, employees, income : int, expenditure : int,inventory : list) -> None:
        super().__init__(name, agrement, employees, income, expenditure)
        self.inventory = inventory

    def check_inventory(self):
        return self.inventory
