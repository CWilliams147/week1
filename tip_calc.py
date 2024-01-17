total_bill = float(input("Total bill amount? $"))
service_level = input("Level of service? ")

tip_percentages = {'good': 0.2, 'fair': 0.15, 'bad': 0.1}

if service_level.lower() in tip_percentages:
    tip_percentage = tip_percentages[service_level.lower()]
    tip_amount = total_bill * tip_percentage
    total_amount = total_bill + tip_amount

    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")
else:
    print("Invalid service level. Please enter 'good', 'fair', or 'bad'.")