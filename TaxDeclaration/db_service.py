import mysql.connector
from persistence_service import PersistenceService
from property import Apartment, Plot, Store
from tax_declaration import TaxDeclaration

class DbService(PersistenceService):

    def __init__(self) -> None:
        try:
            self.conn = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                password = "root1234",
                database = "tax_python")

            self.conn.autocommit = False
            self.cursor = self.conn.cursor(dictionary=True)
        except mysql.connector.Error as error:
            print("Error connecting to database")
            print("Mesage:", error.msg)

    def insert_tax_declaration(self, tax):
        try:
            query = "insert into taxdeclarations(name, surname, vat, " \
                + "phone, submissionYear) values(" \
                + "\'" + tax.name + "\', " \
                + "\'" + tax.surname + "\', " \
                + "\'" + tax.vat + "\', " \
                + "\'" + tax.phone + "\', " \
                + str(tax.submission_year) + ")"
            
            print(query)
            self.cursor.execute(query)

            last_id = self.cursor.lastrowid
            tax.id = last_id

            query_property = ""
            for property in tax.properties:
                if isinstance(property, Apartment):
                    query_property = "insert into apartments(address, surface, " \
                        + "floor, taxDeclarationId) values(" \
                        + "'" + property.address + "', " \
                        + str(property.surface) + ", " \
                        + str(property.floor) + ", " \
                        + str(last_id) + ") "
                elif isinstance(property, Store):
                    query_property = "insert into stores(address, surface, " \
                        + "commerciality, taxDeclarationId) values(" \
                        + "'" + property.address + "', " \
                        + str(property.surface) + ", " \
                        + str(property.commerciality) + ", " \
                        + str(last_id) + ") "
                elif isinstance(property, Plot):
                    query_property = "insert into plots(address, surface, " \
                        + "cultivated, withinCityLimits, taxDeclarationId) values(" \
                        + "'" + property.address + "', " \
                        + str(property.surface) + ", " \
                        + str(property.cultivated) + ", " \
                        + str(property.within_city_limits) + ", " \
                        + str(last_id) + ") "

                self.cursor.execute(query_property)
                last_property_id = self.cursor.lastrowid
                property.id = last_property_id

            self.conn.commit()

        except mysql.connector.Error as error:
            print("Error querying database")
            print("Mesage:", error.msg)            

    def get_tax_declarations(self, vat, submission_year):
        try:
            declarations = []
            query = ""
            if vat == "" and submission_year == 0:
                query = "select * from taxdeclarations"
            elif vat == "" and submission_year != 0:
                query = "select * from taxdeclarations where submissionYear=" \
                    + str(submission_year)
            elif vat != "" and submission_year != 0:
                    query = "select * from taxdeclarations where vat='"+ vat \
                        + "' and submissionYear=" + str(submission_year)
            elif vat != "" and submission_year == 0:
                    query = "select * from taxdeclarations where vat='"+ vat +"'"

            self.cursor.execute(query)

            for row in self.cursor.fetchall():
                declarations.append(TaxDeclaration(row["id"], row["name"], \
                    row["surname"], row["vat"], row["phone"], \
                    row["submissionYear"]))

            for tax in declarations:
                query = "select * from apartments where taxDeclarationId = " \
                    + str(tax.id)
                self.cursor.execute(query)

                for row in self.cursor.fetchall():
                    tax.properties.append(Apartment(row["id"], row["surface"], \
                        row["address"], row["floor"]))

                query = "select * from stores where taxDeclarationId = " \
                    + str(tax.id)
                self.cursor.execute(query)

                for row in self.cursor.fetchall():
                    tax.properties.append(Store(row["id"], row["surface"], \
                        row["address"], row["commerciality"]))

                query = "select * from plots where taxDeclarationId = " \
                    + str(tax.id)
                self.cursor.execute(query)

                for row in self.cursor.fetchall():
                    tax.properties.append(Plot(row["id"], row["surface"], \
                        row["address"], row["withinCityLimits"], row["cultivated"]))
                
            return declarations
        except mysql.connector.Error as error:
            print("Error querying database")
            print("Mesage:", error.msg)            

    def remove_tax_declaration(self, tax):
        try:
            self.cursor.execute("delete from taxdeclarations where vat='"+ \
                tax.vat+"' and submissionYear="+ str(tax.submission_year))

            self.cursor.execute("delete from apartments where taxDeclarationId in " \
                + " (select id from taxDeclarations where vat='"+ \
                tax.vat+"' and submissionYear="+ str(tax.submission_year) + ")")

            self.cursor.execute("delete from stores where taxDeclarationId in " \
                + " (select id from taxDeclarations where vat='"+ \
                tax.vat+"' and submissionYear="+ str(tax.submission_year) + ")")

            self.cursor.execute("delete from plots where taxDeclarationId in " \
                + " (select id from taxDeclarations where vat='"+ \
                tax.vat+"' and submissionYear="+ str(tax.submission_year) + ")")

            self.conn.commit()

        except mysql.connector.Error as error:
            print("Error querying database")
            print("Mesage:", error.msg)            



