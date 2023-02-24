import mysql.connector
from apartment import Apartment
from person import Person
from reservation import Reservation

class PersistenceService:
    def __init__(self) -> None:
        try:
            self.conn = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                password = "root1234",
                database = "test")

            self.conn.autocommit = False
            self.cursor = self.conn.cursor(dictionary=True)
        except mysql.connector.Error as error:
            print("Error connecting to database")
            print("Mesage:", error.msg)

    def get_apartments(self):
        try:
            apartments = []
            self.cursor.execute("select * from Apartments")

            for row in self.cursor.fetchall():
                apartments.append(Apartment(row["id"], row["address"], \
                    row["capacity"], row["price"]))

            return apartments
        except mysql.connector.Error as error:
            print("Error querying database")
            print("Mesage:", error.msg)

    def get_all_reservations(self):
        try:
            reservations = []
            self.cursor.execute("select * from Reservations")

            result_set = self.cursor.fetchall()
            for row in result_set:
                resv = Reservation(row["id"], row["name"], row["surname"], \
                    row["start_date"], row["duration"], row["cost"])

                self.cursor.execute("select * from Persons where reservation_id = " \
                    + str(row["id"]))
                result_set_persons = self.cursor.fetchall()

                for row_person in result_set_persons:
                    resv.add_person(Person(row_person["id"], row_person["name"], \
                        row_person["surname"], row_person["birth_year"]))

                reservations.append(resv)

            return reservations
        except mysql.connector.Error as error:
            print("Error querying database")
            print("Mesage:", error.msg)

    def get_reservations_by_surname(self, surname):
        try:
            reservations = []
            self.cursor.execute("select * from Reservations where surname like \'" \
                + surname + "\'")

            for row in self.cursor.fetchall():
                resv = Reservation(row["id"], row["name"], row["surname"], \
                    row["start_date"], row["duration"], row["cost"])

                self.cursor.execute("select * from Persons where reservation_id = " \
                    + str(row["id"]))
                result_set_persons = self.cursor.fetchall()

                for row_person in result_set_persons:
                    resv.add_person(Person(row_person["id"], row_person["name"], \
                        row_person["surname"], row_person["birth_year"]))

                reservations.append(resv)

            return reservations
        except mysql.connector.Error as error:
            print("Error querying database")
            print("Mesage:", error.msg)

    def insert_reservation(self, reservation):
        try:
            query = "insert into Reservations(name, surname, start_date, " \
                + "duration, cost) values(" \
                + "\'" + reservation.name + "\', " \
                + "\'" + reservation.surname + "\', " \
                + "\'" + str(reservation.start_date) + "\', " \
                + str(reservation.duration) + ", " \
                + str(reservation.cost) + ")"
            
            print(query)
            self.cursor.execute(query)

            last_id = self.cursor.lastrowid
            reservation.id = last_id

            for person in reservation.persons:
                query_person = "insert into Persons(name, surname, " \
                    + "birth_year, reservation_id) values(" \
                    + "\'" + person.name + "\', " \
                    + "\'" + person.surname + "\', " \
                    + str(person.birth_year) + ", " \
                    + str(last_id) + ") "

                self.cursor.execute(query_person)
                last_person_id = self.cursor.lastrowid
                person.id = last_person_id

            self.conn.commit()
        except mysql.connector.Error as error:
            print("Error saving to database. Performing rollback..")
            print("Mesage:", error.msg)
            self.conn.rollback()
