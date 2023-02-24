from abc import ABC, abstractmethod

class PersistenceService(ABC):
    @abstractmethod
    def insert_tax_declaration(self, tax):
        pass

    @abstractmethod
    def get_tax_declarations(self, vat, submission_year):
        pass

    @abstractmethod
    def remove_tax_declaration(self, tax):
        pass



