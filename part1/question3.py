################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
# def make_oven():
#   None

class MagicalOven:
    def __init__(self):
        """
        Initialize a MagicalOven object with an empty list of ingredients.
        """
        self.ingredients = []

    def add(self, item):
        """
        Add an item to the list of ingredients.

        Args:
            item (str): The name of the ingredient to be added.
        """
        self.ingredients.append(item)

    def freeze(self):
        """
        Freeze the ingredients in the oven if they are water and air, otherwise set them to "Frozen Material."
        """
        if "water" in self.ingredients and "air" in self.ingredients:
            self.ingredients = ["snow"]
        else:
            self.ingredients = ["Frozen Material"]

    def boil(self):
        """
        Boil the ingredients in the oven. If it's lead and mercury, set them to "gold." 
        If it's cheese, dough, and tomato, set them to "pizza." Otherwise, set them to "Boiled Material."
        """
        if "lead" in self.ingredients and "mercury" in self.ingredients:
            self.ingredients = ["gold"]
        elif "cheese" in self.ingredients and "dough" in self.ingredients and "tomato" in self.ingredients:
            self.ingredients = ["pizza"]
        else:
            self.ingredients = ["Boiled Material"]

    def wait(self):
        """
        Implement a waiting method by setting the ingredients to "Combined Material."
        """
        self.ingredients = ["Combined Material"]

    def get_output(self):
        """
        Get the first ingredient in the oven's list.

        Returns:
            str: The first ingredient in the list.
        """
        return self.ingredients[0]

def make_oven():
    """
    Create and return a MagicalOven instance.

    Returns:
        MagicalOven: An instance of the MagicalOven class.
    """
    return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
    """
    Combine ingredients in the oven based on the provided temperature.

    Args:
        oven (MagicalOven): The oven in which to combine the ingredients.
        ingredients (list): List of ingredients to combine.
        temperature (int): The temperature for the combination process.
        
    Returns:
        str: The result of the alchemical combination.
    """
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()
