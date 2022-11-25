# Exercise 7:

#Create a function with a default argument
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 2000 to salary

def show_employee(name, salary=2000):
    print("Name:", name, "salary:", salary)

show_employee("fatima", 1000)
show_employee("Jessica")