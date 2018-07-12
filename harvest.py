############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""
    reporting_code = None
    name = None
    first_harvest = None
    color = None
    pairs = []
    seeds = False
    is_bestseller = False


    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.reporting_code = code
        self.first_harvest = first_harvest
        self.color = color
        self.pairs = []
        self.seeds = is_seedless
        self.is_bestseller = is_bestseller


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairs.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.reporting_code = new_code




def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint') 
    all_melon_types.append(musk)

    casaba = MelonType('cas', "Casaba", 2003, 'orange', False, False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', "Yellow Watermelon", 2013, 'yellow', False, True)
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

make_melon_types()
# print (musk.name) 
# print (casaba.name) 


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print("{melon} pairs with /n {pairs}".format(melon = self.name))

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


