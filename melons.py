"""This file should have our melon-type classes in it."""

# Creates a new class for each melon type.
# Creates methods to calcualte cost for each melon, passing
# quantity.

class MelonOrder(object):
    species = None
    color = None
    imported = False
    shape = None
    seasons = None
    base_cost = 5

    # def set_base_cost(self, new_base):
    #     base_cost = new_base
    #     return base_cost

class WatermelonOrder(MelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        total = self.base_cost * qty

        return total
        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        total = self.base_cost * qty

        if qty >= 3:
            total *= 0.75

        return total


class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        total = self.base_cost * qty

        if qty >= 5:
            total *= 0.5

        return total


class CasabaOrder(object):
    species = 'Casaba'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        return total


class SharlynOrder(object):
    species = 'Sharlyn'
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        total = self.base_cost * qty

        return total


class SantaClausOrder(object):
    species = 'Santa_Claus'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        total = self.base_cost * qty

        return total


class ChristmasOrder(object):
    species = 'Christmas'
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        total = self.base_cost * qty

        return total


class HornedMelonOrder(object):
    species = 'Horned_Melon'
    color = 'yellow'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        total = self.base_cost * qty

        return total


class XiguaOrder(object):
    species = 'Xigua'
    color = 'black'
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        total = self.base_cost * qty

        return total


class OgenOrder(object):
    species = 'Ogen'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0

        if self.species == "Ogen" or self.species == "Casaba":
            self.base_cost += 1
        if self.imported:
            self.base_cost *= 1.5
        if self.shape == 'square':
            self.base_cost *= 2

        total = self.base_cost * qty

        return total