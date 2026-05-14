# Calculate gross pay with overtime

# Define variables
pay_rate = 17.50
hours = 45
filing_status = "single"

# Calculate gross pay
if hours > 40:
    overtime_hours = hours - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours * pay_rate

print(f"You worked {hours} hours at ${pay_rate} per hour")
print(f"Your gross pay is ${format(gross_pay, '.2f')}")
