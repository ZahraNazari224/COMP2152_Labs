#Question 4: Class Attendance (Sets - Uniqueness and Operations)
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")
print("Monday Class: ", monday_class)
print("Wednesday Class: ", wednesday_class)

both_classes= monday_class & wednesday_class
print("Attended both classes: ", both_classes)

allStudents = monday_class | wednesday_class
print("Attended either class: ", allStudents)

only_monday = allStudents - wednesday_class
print("Only Monday class: ", only_monday)

onlyOne = monday_class ^ wednesday_class
print("Only one class: ", onlyOne)

print("Is Monady subset of all students? ", monday_class <= allStudents)
