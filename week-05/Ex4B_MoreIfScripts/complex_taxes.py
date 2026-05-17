# Calculate federal tax based on income and filing status

hours_worked = 40
pay_rate = 15
filing_status = "single" # Change to test different values

weekly_gross = hours_worked * pay_rate
annual_gross = weekly_gross * 52

if filing_status == "single":
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == "joint":
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

weekly_tax = weekly_gross * tax_rate
net_pay = weekly_gross - weekly_tax

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate} per hour, your gorss weekly pay is ${weekly_gross}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${round(weekly_tax, 2)}")
print(f"Your net pay is ${round(net_pay, 2)}")

