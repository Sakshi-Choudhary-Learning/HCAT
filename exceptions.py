'''
Assignment 5:

Part 1: Exception Handling

File: exceptions.py

Ask the user for hours worked and handle if input is invalid.

Create safe_productivity_score(tasks_completed, hours_worked) function:

Score = tasks_completed / hours_worked

Return an appropriate message when an error occurs.


Part 2: Git Workflow

Initialize a Git repository using git init.

Add all project files to the repository.

Create at least three commits:

Commit 1: basic employee data

Commit 2: employee and task management

Commit 3: analytics and exception handling

Push the project to GitHub. Gitbash installation: 

'''


def safe_productivity_score(tasks_completed, hours_worked):
    try:
        score = tasks_completed / hours_worked
        return f"Productivity Score: {score}"
    except ZeroDivisionError:
        return "Error: Hours worked cannot be zero."
    except TypeError:
        return "Error: Invalid data type."
    except Exception as e:
        return f"Unexpected error occurred: {e}"


try:
    hours = float(input("Enter hours worked: "))
    tasks = int(input("Enter tasks completed: "))

    result = safe_productivity_score(tasks, hours)
    print(result)

except ValueError:
    print("Error: Please enter valid numeric values.")
