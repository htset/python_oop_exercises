from datetime import date, datetime
from apartment import Apartment
from person import Person
from reservation import Reservation

class UIService:
    def __init__(self, persistence_service) -> None:
        self.persistence_service = persistence_service

    def menu(self):
        option = 0
        while True:
            print("\nOptions")
            print("1) Add reservation ")
            print("2) Search reservation ")
            print("3) View all reservations ")
            print("0) Exit ")
            option = int(input())

            match option:
                case 1:
                    self.add_reservation()
                case 2:
                    self.search_reservation()
                case 3:
                    self.list_reservations()
                case 0:
                    break
                case _:
                    print("please try again")
        
    
    def add_reservation(self):
        print("Name: ")
        name = input()
        print("Surname: ")
        surname = input()
        print("Start date: ")
        start_date = datetime.strptime(input(), '%Y-%m-%d').date()
        print("Duration (days):")
        duration = int(input())

        print("Available apartments:")
        apartments = self.persistence_service.get_apartments()

        i = 1
        for apartment in apartments:
            print("Apartment no.: ", i)
            print(apartment)
            i = i + 1

        print("Press 0 to cancel")
        option = int(input())

        if option > 0 and option <= len(apartments):
            resv = Reservation(0, name, surname, start_date, duration, \
                apartments[option-1].price * duration)
            self.add_persons(resv)
            self.persistence_service.insert_reservation(resv)

    def search_reservation(self):
        print("Enter surname (also partial): ")
        surname = input()
        for p in self.persistence_service.get_reservations_by_surname(surname):
            print(p)

    def list_reservations(self):
        for p in self.persistence_service.get_all_reservations():
            print(p)

    def add_persons(self, reservation):
        while True:
            print("Name: ")
            name = input()
            print("Surname: ")
            surname = input()
            print("Birth year: ")
            birth_year = int(input())

            reservation.add_person(Person(0, name, surname, birth_year))

            print("Add another person? (y/n)")
            option = input()

            if option == "n":
                return
