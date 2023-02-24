class TaxDeclaration:
    def __init__(self, id=0, name="", surname="", vat="", phone="",submission_year=0 ) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.vat = vat
        self.phone = phone
        self.submission_year = submission_year
        self.properties = []

    def __str__(self):
        ret = "VAT: " + self.vat + "\nSurname: " + self.surname + "\nName: " + self.name \
            + "\nPhone: " + self.phone + "\nSubmission year: " + str(self.submission_year) \
            + "\nTax: " + str(self.calculate_tax()) +"\n"
        for property in self.properties:
            ret += property.__str__()
        ret += "---\n"
        return ret

    def add_property(self, property):
        self.properties.append(property)

    def calculate_tax(self):
        tax = 0
        for property in self.properties:
            tax += property.calculate_tax()
        return tax


            


    