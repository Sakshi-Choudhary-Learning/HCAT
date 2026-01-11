'''
Assignment 1:
Basic Employee Data (Variables, Data Types)
File: employee_data.py
Create variables for one employee:
employee_id (int)
name (string)
hourly_rate (float)
is_active (boolean)
Print the values and their data types.
Convert hourly_rate to an integer and print the result.
'''


# Employee data variables
employee_id = 101
name = "Sakshi Choudhary"
hourly_rate = 250.75
is_active = True

# Print values and their data types
print("Employee ID:", employee_id, "Type:", type(employee_id))
print("Name:", name, "Type:", type(name))
print("Hourly Rate:", hourly_rate, "Type:", type(hourly_rate))
print("Is Active:", is_active, "Type:", type(is_active))

# Convert hourly_rate to integer
hourly_rate_int = int(hourly_rate)
print("Hourly Rate (Integer):", hourly_rate_int, "Type:", type(hourly_rate_int))
