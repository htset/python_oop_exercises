from datetime import date
from derived import BasePackage, AdvancedPackage, OvernightPackage
import os

class UIService:

    def __init__(self) -> None:
        self.packages = []
        self.load_from_file()

    def menu(self):
        option = 0
        while True:
            print("\nOptions")
            print("1) Add package ")
            print("2) Search package ")
            print("3) Delete package ")
            print("4) View all packages ")
            print("0) Exit ")
            option = int(input())

            match option:
                case 1:
                    self.add_package()
                case 2:
                    self.search_package()
                case 3:
                    self.delete_package()
                case 4:
                    self.list_packages()
                case 0:
                    break
                case _:
                    print("please try again")

    def add_package(self):
        print("\nType of package (1-Basic, 2-Advanced, 3-Overnight)")
        option = int(input())
        print("Recipient name: ")
        recipient_name = input()
        print("Recipient address: ")
        recipient_address = input()
        print("Weight (kilos):")
        weight = int(input())

        match option:
            case 1:
                self.packages.append(BasePackage(recipient_name, \
                    recipient_address, weight, date.today()))
                self.save_to_file()
            case 2:
                self.packages.append(AdvancedPackage(recipient_name, \
                    recipient_address, weight, date.today()))
                self.save_to_file()
            case 3:
                self.packages.append(OvernightPackage(recipient_name, \
                    recipient_address, weight, date.today()))
                self.save_to_file()
            case _:
                print("invalid option")

    def search_package(self):
        print("Enter recipient name (also partial): ")
        recipient_name = input()
        for p in self.packages:
            if p.recipient.find(recipient_name) >= 0:
                print(p)

    def delete_package(self):
        print("Enter recipient name (also partial): ")
        recipient_name = input()
        print("The following packages were found: ")
        i = 0
        for p in self.packages:
            i += 1
            if p.recipient.find(recipient_name) >= 0:
                print(str(i) + ") " + str(p))

        print("Please enter the no. of package to delete (0 to cancel): ")
        option = int(input())

        if option > 0:
            self.packages.pop(i - 1)
            print("package deleted")
            self.save_to_file()

    def list_packages(self):
        for p in self.packages:
            print(p)
            print("---")

    def save_to_file(self):
        file = open('packages.txt', 'w')
        for p in self.packages:
            file.write(p.serialize())
        file.close()
            
    def load_from_file(self):
        try:
            if not os.path.isfile('packages.txt'):
                return

            file = open('packages.txt', 'r')
            package_str = ""
            lines = file.readlines()
            for line in lines:
                if line == "---\n":
                    if package_str.find("BasePackage") >= 0:
                        p = BasePackage()
                        p.deserialize(package_str)
                        self.packages.append(p)
                    elif package_str.find("AdvancedPackage") >= 0:
                        p = AdvancedPackage()
                        p.deserialize(package_str)
                        self.packages.append(p)
                    elif package_str.find("OvernightPackage") >= 0:
                        p = OvernightPackage()
                        p.deserialize(package_str)
                        self.packages.append(p)
                    package_str = ""
                else:
                    package_str = package_str + line

        except Exception as ex:
            print("error loading file")
        


