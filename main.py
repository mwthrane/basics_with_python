# float, number with decimals e.g. 2.5

# Variables
calculation_to_seconds = 24 * 60 * 60

calculation_to_units = 24 * 60 * 60
name_of_unit = "hours"
# print str with number(int). f = format
print(f"20 days are {20 * calculation_to_seconds} seconds")
print(f"20 days are {20 * calculation_to_units} {name_of_unit}")

# Functions
# Variables defined in the function is only avail in that function


def days_to_units(number_of_days, custom_message):
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


days_to_units(80, "Good!")

# Accept user input and convert string to int.
# Check the value is > 0 and check the type


def days_to_units(number_of_days):
    conditional_check = number_of_days > 0
    print(type(conditional_check))
    try:
        if number_of_days > 0:
            return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}"
        elif number_of_days == 0:
            return "please enter a positive number, exiting!"
    except ValueError:
        return "you entered a negative value, exiting!"


user_input = input("Enter a number of days and I will calculate the hours\n")

if user_input.isdigit():
    user_input_number = int(user_input)
    calculated_value = days_to_units(user_input_number)
    print(calculated_value)
else:
    print("Your input is not a number")
