##Exercise 6:
#  Assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)

# call using original name
display_student("fatima", 19)

# assign new name
showStudent = display_student
# call using new name
showStudent("fat7ima", 19)
