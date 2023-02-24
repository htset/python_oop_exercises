from tax_declaration import TaxDeclaration
from property import Apartment, Store, Plot

class UIService:
    def __init__(self, persistence_service, statistics_service) -> None:
        self.persistence_service = persistence_service
        self.statistics_service = statistics_service

    def menu(self):
        option = 0
        while True:
            print("\nOptions")
            print("\---Transactions---")
            print("1) Add new tax declaration ")
            print("2) Delete tax declaration ")
            print("3) Find tax declaration ")
            print("\---Statistics---")
            print("11: Get total tax")
            print("12: Get Tax Declaration with highest tax ")
            print("\n0) Exit ")
            option = int(input())

            match option:
                case 1:
                    self.create()
                case 2:
                    self.remove()
                case 3:
                    self.search()
                case 11:
                    print("Total Tax is: ", self.statistics_service.get_total_tax())
                case 12:
                    print("Highest Tax Declaration is: ", \
                        self.statistics_service.get_highest_declaration())
                case 0:
                    break
                case _:
                    print("please try again")

    def create(self):
        print("Enter person details:")
        print("Name:")
        name = input()
        print("Surname:")
        surname = input()
        print("VAT:")
        vat = input()
        print("Telephone:")
        phone = input()
        print("Fiscal year:")
        year = int(input())

        tax = TaxDeclaration(0, name, surname, vat, phone, year)

        print("Now enter properties:")
        option = 'y'
        while option == 'y':
            print("Select 1 for Apartment, 2 for Store, 3 for Plot, any other to abort: ")
            selection = int(input())
            match selection:
                case 1:
                    print("Surface:")
                    surface = int(input())
                    print("Address:")
                    address = input()
                    print("Floor:")
                    floor = int(input())
                    tax.add_property(Apartment(0, surface, address, floor))
                case 2:
                    print("Surface:")
                    surface = int(input())
                    print("Address:")
                    address = input()
                    print("Commerciality:")
                    commerciality = int(input())
                    tax.add_property(Store(0, surface, address, commerciality))
                case 3:
                    print("Surface:")
                    surface = int(input())
                    print("Address:")
                    address = input()
                    print("Is inside town limits (y/n):")
                    within_city_limits = input()
                    if within_city_limits == 'y':
                        within_city_limits = True
                    else:
                        within_city_limits = False
                    print("Is cultivated (y/n):")
                    cultivated = input()
                    if cultivated == 'y':
                        cultivated = True
                    else:
                        cultivated = False

                    tax.add_property(Plot(0, surface, address, within_city_limits, \
                        cultivated))

            print("Would you like to add another property? (y/n)")
            selection = input()

            if selection != 'y':
                break

        self.persistence_service.insert_tax_declaration(tax)
        print("Tax declaration added")

    def remove(self):
        print("Enter VAT: ")
        vat = input()
        print("enter submission year:")
        submission_year = int(input())
        declarations = self.persistence_service.get_tax_declarations(vat, submission_year)

        if(len(declarations) == 1):
            print("Found tax declaration: ")
            print(declarations[0])
            print("Delete tax declaration? (y/n)")
            sel = input()
            if(sel == 'y'):
                self.persistence_service.remove_tax_declaration(declarations[0])
                print("Tax delcaration deleted successfully")
            else:
                print("tax declaration not found")
        elif(len(declarations) == 0):
            print("No tax declaration was found")
        elif(len(declarations) > 1):
            print("Error: More than one tax declarations were found!")

    def search(self):
        print("Enter VAT: ")
        vat = input()
        print("enter submission year (press 0 for all years):")
        submission_year = int(input())
        declarations = self.persistence_service.get_tax_declarations(vat, submission_year)

        if len(declarations) > 0:
            print("--Tax declarations--")
            for td in declarations:
                print(str(td))
        else:
            print("No tax declarations were found")
        



        

