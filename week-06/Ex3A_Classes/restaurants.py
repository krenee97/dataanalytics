# Working with classes - Resturants

class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# Create three instances
rest1 = Restaurant("McDonald's", "fast food")
rest2 = Restaurant("Olive Garden", "Italian food")
rest3 = Restaurant("Nobu", "Japanese food")

#Call methods for each instance
rest1.describe_rest()
rest1.rest_open()

rest2.describe_rest()
rest2.rest_open()

rest3.describe_rest()
rest3.rest_open()