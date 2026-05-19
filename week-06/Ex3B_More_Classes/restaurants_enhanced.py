# More fun with classes - Enhanced Restaurant

class Restaurant:
    """A class to represent a restaurant"""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_servered = 0 
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        served = int(input("How many customers served today?"))
        self.number_servered += served

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_servered} customers.")

    def customer_rating(self):
        rating = int(input("How would you rate your experience today on a scale of 1-5? "))
        self.customer_ratings.append(rating)
        avg = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f"Your rating was {rating}. The avgerage rating this resturant is {avg}.")


# Create three instances 
rest1 = Restaurant("McDonald's", "fast food")
rest2 = Restaurant("Olive Garden", "Italian food")
rest3 = Restaurant("Nobu", "Japanese food")

# Test print_num_served
rest1.print_num_served()
rest1.add_num_served()
rest1.add_num_served()
rest1.print_num_served()

# Test customer_rating
rest1.customer_rating()
rest1.customer_rating()
rest1.customer_rating()