
# 1. Create two sets
python_students = {"Asha", "Rahul", "Anu"}
data_science_students = {"Rahul", "Anu", "Arun"}

# 2. Add a new student to the Python set
python_students.add("Neha")

# 3. Remove one student from the Data Science set
data_science_students.remove("Arun")

# 4. Find students enrolled in both courses
both_courses = python_students.intersection(data_science_students)
print("Students in both courses:", both_courses)

# 5. Find students only in Python
python_only = python_students.difference(data_science_students)
print("Students only in Python:", python_only)

# 6. Display all students without duplicates
all_students = python_students.union(data_science_students)
print("All students:", all_students)

# 7. Create a dictionary with course names and student counts
course_students = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

# 8. Print course names and student counts using a loop
for course, count in course_students.items():
    print(f"Course: {course}, Students: {count}")

# 9. Double the student counts using dictionary comprehension
expected_growth = {
    course: count * 2
    for course, count in course_students.items()
}

print("Expected growth:", expected_growth)
