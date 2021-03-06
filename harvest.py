# ############
# # Part 1   #
# ############


class MelonType(object):
    """A species of melon at a melon farm."""


    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        self.name = name
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

    def __repr__(self):
        return (f'{self.name}')



def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('Muskmelon', 'musk', 1998, 'green', True, True)
    musk.add_pairing('mint') 
    all_melon_types.append(musk)

    casaba = MelonType("Casaba", 'cas', 2003, 'orange', False, False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('Crenshaw', 'cren', 1996, 'green', False, False)
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("Yellow Watermelon", 'yw', 2013, 'yellow', False, True)
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for food in melon.pairs:
            print(f'- {food}')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dictioary = {}
    #keys- reporting codes
    #values- instance

    for melon in melon_types:
        melon_dictioary[melon.reporting_code] = melon

    return melon_dictioary






############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
        #Probably Maybe
        #go through list of all the melons, check melon.type matches a key in the dictionary (melon_types) then add the melon_type attributes to the melon object

    def check_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False
    
    def __repr__(self):
        return (f'{self.type}, {self.shape_rating}')


def make_melons(melon_types):
    """Returns a list of Melon objects"""

    all_melons = []

    Melon_1 = Melon("yw", 8,7,2,"Sheila")
    all_melons.append(Melon_1)

    Melon_2 = Melon("yw", 3,4,2, "Sheila")
    all_melons.append(Melon_2)

    Melon_3 = Melon("yw",9,8,3,"Sheila")
    all_melons.append(Melon_3)

    Melon_4 = Melon("cas",10,6,35, "Sheila")
    all_melons.append(Melon_4)

    Melon_5 = Melon("cren",8,9,35, "Michael")
    all_melons.append(Melon_5)

    Melon_6 = Melon("cren",8,2,35, "Michael")
    all_melons.append(Melon_6)

    Melon_7 = Melon("cren",2,3,4, "Michael")
    all_melons.append(Melon_7)

    Melon_8 = Melon("musk",6,7,4, "Michael")
    all_melons.append(Melon_8)

    Melon_9 = Melon("yw",7,10,3, "Sheila")
    all_melons.append(Melon_9)

    return all_melons




def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


def execute_melon_functions():
    all_melon_types = make_melon_types()
    melon_dictionary = make_melon_type_lookup(all_melon_types)
    make_melons(melon_dictionary)



