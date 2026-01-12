'''Assignment 3

Operations and Control Flow
File: logic.py
Ask the user to input hours worked.
Use if/elif/else to classify:
Underworked (<20 hours)
Normal (20–40 hours)
Overtime (>40 hours)
Use a for loop to print all employee names.
Use a while loop to repeatedly ask for a task until the user types ""done"".
'''


# Ask the user to input hours worked.
hours_worked=int(input("Enter Worked Hours: "))

#Use if/elif/else to classify:
if hours_worked<20:
    print("Status: Underworked")
elif 20 <= hours_worked <=40:
    print("Status: Normal")
else:
    print("Status: Overtime") 
print("-" * 50)    

# Use a for loop to print all employee names.    
employee_names = ["Sakshi","Samarth","Shubhangi","Neha","Swapna","Amit"]
print("Employee Names: ")
for name in employee_names:
    print(name)
print("-" * 50) 


#Use a while loop to repeatedly ask for a task until the user types ""done"".
#tasks=[]
while True:
    task= input("Enter a task (type 'done' to stop): ")
    if task.lower() == "done":
        print("-" * 50) 
        print("Task Entery Completed Successfully.")
        print("-" * 50) 
        break
    else:
        #tasks.append(task)
        print(f"Task Added: {task}")


#print("All Entered Tasks: ")
#for t in tasks:
#    print("-", t)
#print("-" * 50)     








