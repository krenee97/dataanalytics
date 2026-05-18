# More functions - mailing label, add numbers, display receipt

def display_mailing_label(name, address, city, state, zip):
    print(f"{name}")
    print(f"{address}")
    print(f"{city}, {state} {zip}")

def add_numbers(*args):
    total = sum(args)
    numbers = " + ".join(str(n) for n in args)
    print(f"{numbers} = {total}")

def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")
    if amount_paid >= total_due:
        change =  amount_paid - total_due
        print(f"Change Due: ${change}")
    else: 
        remaning = total_due - amount_paid
        print(f"Remaning balance to be apid: ${remaning}")
    
# Test display_mailing_label
display_mailing_label("Kendra Tyler", "1421 4th St", "Glenarden", "MD", "20706")
display_mailing_label("Bernie Mac", "425 Oak Ave", "Atlanta", "GA", "30301")

#Test add_numbers
add_numbers(5)
add_numbers(3, 7)
add_numbers(10, 20, 30, 40)

# Test display_receipt
display_receipt(50, 60) # overpay
display_receipt(50, 50) # exact
display_receipt(50, 30) # underpay
