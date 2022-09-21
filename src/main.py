#Oskar Svedlund
#TEINF-20
#2022-09-15
#Class exercise

from resources import Establishment, Shop, Resturant

test1 = Shop("test_1", "undecided", ["marget", "elias", "markus"], 100, 50,["idk", "apples"])

def main():

    while True:
        choice = input("1. check name\n2. check agreement\n3. check employies\n4. Hire additional employees\n#. exit\n>> ")

        if choice == "1":
            print(test1.name)

        elif choice == "2":
            print(test1.agrement)

        elif choice == "3":
            print(test1.employees)

        elif choice == "4":
            test1.hire_staff()

        elif choice == "#":
            break


if __name__ == "__main__":
    main()