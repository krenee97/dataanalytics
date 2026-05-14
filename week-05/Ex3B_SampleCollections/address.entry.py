# Address entry execrise - dictionary

contact_info = { 
    "name": "Kendra Tyler",
    "address": "1421 4th street",
    "city": "Glenarden",
    "state": "MD",
    "zip": "20706"
}

# Step2: print formatted address
print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']},{contact_info['state']}{contact_info['zip']}")

# Step 3: remove name key
del contact_info["name"]

# Step 4: add first and last name separately
contact_info["first_name"] = "Kendra"
contact_info["last_name"] = "Tyler"

# Step 5: add honorific
contact_info.update({"honorific": "Ms."})

# Step 6: add full name
contact_info["full_name"] = contact_info["honorific"] + " " + contact_info["first_name"] + " " + contact_info["last_name"]

# Step 7: print updated address
print(f"{contact_info['full_name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")
