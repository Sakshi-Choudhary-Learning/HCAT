'''Assignment 2:

Managing Employees and Tasks (Lists, Dictionaries, Sets, Tuples)
File: management.py

2.1 List of Employees
Create a list of employee dictionaries.
Add a new employee to the list.
Remove an employee from the list.
Print the total number of employees.

2.2 Task Dictionary
Create a dictionary where keys are employee IDs and values are lists of assigned tasks.
Add a task to an employee.
Remove a task from an employee.
Print all tasks for all employees.

2.3 Unique Skills Using Sets
Create a set containing all unique employee skills.
Add two new skills to the set.
Print the final set of skills.

2.4 Company Holidays Using Tuples
Create a tuple of company holiday dates.
Attempt to change an element and if it fails, Write a comment explaining it.
'''


''''

# 2.1 List of Employees


employees = [
    {"id": 101, "name": "Sakshi", "role": "Cloud Engineer"},
    {"id": 102, "name": "Samarth", "role": "Developer"},
    {"id": 103, "name": "Priti", "role": "Tester"}
]

new_employee = {"id": 104, "name": "Raj", "role": "DevOps Engineer"}
employees.append(new_employee)

employees = [emp for emp in employees if emp["id"] != 102]

print("Total Employees:", len(employees))
print("Employee List:", employees)




# 2.2 Task Dictionary

tasks = {
    101: ["Monitor AWS resources", "Create CloudWatch alarms"],
    103: ["Test application", "Log bugs"],
    104: ["Setup CI/CD pipeline"]
}

tasks[101].append("Optimize cost")


tasks[103].remove("Log bugs")


print("\nEmployee Tasks:")
for emp_id, task_list in tasks.items():
    print(f"Employee {emp_id}: {task_list}")





# 2.3 Unique Skills Using Sets


skills = {"AWS", "Python", "Linux", "Docker"}

skills.add("Terraform")
skills.add("Kubernetes")

print("\nUnique Skills:", skills)

'''

# 2.4 Company Holidays Using Tuples


holidays = ("2026-01-26", "2026-08-15", "2026-10-02")

print("\nCompany Holidays:", holidays)

