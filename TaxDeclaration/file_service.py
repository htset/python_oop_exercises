import os
import jsonpickle
from persistence_service import PersistenceService

class FileService(PersistenceService):
    def __init__(self) -> None:
        super().__init__()
        self.declarations  = []
        self.load_from_file()

    def insert_tax_declaration(self, tax):
        self.declarations.append(tax)
        self.save_to_file()

    def get_tax_declarations(self, vat, submission_year):
        if vat == "" and submission_year == 0:
            return self.declarations

        ret = []
        for td in self.declarations:
            if vat != "":
                if submission_year != 0:
                    if td.vat == vat and td.submission_year == submission_year:
                        ret.append(td)
                else:
                    if td.vat == vat:
                        ret.append(td)
            else:
                if submission_year != 0:
                    ret.append(td)
        return ret

    def remove_tax_declaration(self, tax):
        for td in self.declarations:
            if td.vat == tax.vat and td.submission_year == tax.submission_year:
                self.declarations.remove(td)
        
        self.save_to_file()
    
    def load_from_file(self):
        try:
            if not os.path.isfile('tax_declarations.json'):
                return

            file = open('tax_declarations.json', 'r')
            json = file.readline()
            self.declarations = jsonpickle.decode(json)

        except Exception as ex:
            print("error loading file")
 
    def save_to_file(self):
        file = open("tax_declarations.json", "w")
        json = jsonpickle.encode(self.declarations)
        file.write(json)
        file.close()
