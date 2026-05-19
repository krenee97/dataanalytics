# Optional Lab 2 - Rewards Program class

cust_list = []

class RewardsProgram:
    """A class to represent a customer rewards program."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))

# Create three instances
cust1 = RewardsProgram("Kendra Tyler", "586-0950", "kendrat@email.com")
cust2 = RewardsProgram("Berine Mac", "555-5678", "berinem@email.com")
cust3 = RewardsProgram("Jane Sliver", "567-7865", "janes@email.com")

# Run methods for each customer
for cust in [cust1, cust2, cust3]:
    cust.profile()
    cust.thank_you()
    cust.add_to_cust_list()
    print()

# Print the full customer list
print("Customer List:")
print(cust_list)