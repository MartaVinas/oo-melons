"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        if self.species.lower() == "christmas melon":
            base_price = 5 * 1.5
        else:
            base_price = 5
        
        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    country_code = "USA"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

    def get_total(self):
        total = super().get_total()
        
        if self.qty < 10:
            return total + 3
        else:
            return total

class GovernmentMelonOrder(AbstractMelonOrder):
    order_type = "domestic"
    country_code = "USA"
    tax = 0.0
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True
        else:
            self.passed_inspection = False


   
