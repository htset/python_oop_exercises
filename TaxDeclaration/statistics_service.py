class StatisticsService:
    def __init__(self, persistence_service) -> None:
        self.persistence_service = persistence_service

    def get_total_tax(self):
        total_tax = 0
        declarations = self.persistence_service.get_tax_declarations("", 0)
        for tax in declarations:
            total_tax += tax.calculate_tax()

        return total_tax

    def get_highest_declaration(self):
        declarations = self.persistence_service.get_tax_declarations("", 0)
        if len(declarations) > 0:
            max_tax = declarations[0]
            max_tax_value = max_tax.calculate_tax()
            
            for tax in declarations:
                if tax.calculate_tax() > max_tax_value: 
                    max_tax = tax

            return max_tax

