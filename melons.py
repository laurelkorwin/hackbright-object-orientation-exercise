"""This file should have our order classes in it."""

import random

class TooManyMelonsError(ValueError):
    pass

class AbstractMelonOrder(object):
    """Abstract parent class for melon orders."""
    
    shipped = False

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes"""
        if qty > 100:
            raise TooManyMelonsError("Orders cannot exceed 100 melons.")
        self.qty = qty
        self.species = species
        if country_code:
            self.country_code = country_code

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        """Calculate base price."""
        return random.randint(5,9)

    def get_total(self):
        """Calculate total price."""
        base_price = self.get_base_price()
        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    country_code = "USA"
    order_type = "domestic"
    tax = 0.08
    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def get_total(self):
        flat_fee = 3
        subtotal = super(InternationalMelonOrder, self).get_total()
        if self.qty >= 10:
            total = subtotal
        else:
            total = subtotal + flat_fee
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """Secret government melon order."""

    order_type = "government"
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
