'''
Assignment-4 Part 4: Functions for Productivity Analysis
File: analytics.py
Function: calculate_pay(hours, rate)
Return total pay.
Function: employee_statistics(hours_list)
Return max, min, and average hours.
Function: search_employee(employees, emp_id)
Return employee details if found, otherwise ""Employee not found"".
'''


# Function to calculate total pay
def calculate_pay(hours, rate):
    
    #Calculate total pay based on hours worked and hourly rate.
    
    return hours * rate


# Function to calculate employee statistics
def employee_statistics(hours_list):
    
   # Return maximum, minimum, and average hours from a list.

    if not hours_list:
        return 0, 0, 0

    max_hours = max(hours_list)
    min_hours = min(hours_list)
    avg_hours = sum(hours_list) / len(hours_list)

    return max_hours, min_hours, avg_hours


# Function to search for an employee by ID
def search_employee(employees, emp_id):
    
    #Search employee details by employee ID.
    
    for employee in employees:
        if employee.get("id") == emp_id:
            return employee

    return "Employee not found"
employees = [
    {"id": 101, "name": "Sakshi", "hours": 40},
    {"id": 102, "name": "Choudhary", "hours": 35}
]
print(calculate_pay(40, 500))  
print(employee_statistics([50, 45, 50, 30]))
print(search_employee(employees, 102))