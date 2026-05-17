# Sampling tools using the random module 

import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

#a) Products of the Day - randonmly select one product
product_of_day = random.choice(products)
print(f"Products of the Day: {product_of_day}")

#b) Usebility survey - select 3 products without replacemnt 
survey_products = random.sample(products, 3)
print(f"Survey products: {survey_products}")

#c) Randomized display - shuffle the products list
random.shuffle(products)
print(f"Randonized product list: {products}")

#d) Simulated daily transaction count between 50 and 300
transaction_count = random.randiant(50, 300)
print(f"Daily transaction count: {transaction_count}")
