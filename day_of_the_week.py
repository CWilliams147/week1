def get_day_of_week(day):
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    if 0 <= day <= 6:
        return days_of_week[day]
    else:
        return "Invalid day"

try:
    day_input = int(input("Day (0-6)? "))
    day_of_week = get_day_of_week(day_input)
    print(day_of_week)
except ValueError:
    print("Please enter a valid Number")