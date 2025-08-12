from models.student import Student
from models.course import Course

def add_new_student(students):
    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    address = input("Enter Address: ").strip()
    student_id = input("Enter Student ID: ").strip()

    if student_id in students:
        print(f"Student ID {student_id} already exists.")
        return
    if not age.isdigit():
        print("Invalid age.")
        return

    student = Student(name, int(age), address, student_id)
    students[student_id] = student
    print(f"Student {name} (ID: {student_id}) added successfully.")

def add_new_course(courses):
    course_name = input("Enter Course Name: ").strip()
    course_code = input("Enter Course Code: ").strip()
    instructor = input("Enter Instructor: ").strip()

    if course_code in courses:
        print(f"Course Code {course_code} already exists.")
        return

    course = Course(course_name, course_code, instructor)
    courses[course_code] = course
    print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

def enroll_student_in_course(students, courses):
    student_id = input("Enter Student ID: ").strip()
    course_code = input("Enter Course Code: ").strip()

    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    if course_code not in courses:
        print(f"Course Code {course_code} does not exist.")
        return

    student = students[student_id]
    course = courses[course_code]

    if course_code in student.courses:
        print(f"Student {student.name} (ID: {student_id}) already enrolled in {course.course_name}.")
        return

    student.enroll_course(course_code)
    course.add_student(student_id)
    print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")

def add_grade_for_student(students, courses):
    student_id = input("Enter Student ID: ").strip()
    course_code = input("Enter Course Code: ").strip()
    grade = input("Enter Grade: ").strip()

    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    if course_code not in courses:
        print(f"Course Code {course_code} does not exist.")
        return

    student = students[student_id]

    if course_code not in student.courses:
        print(f"Student {student.name} (ID: {student_id}) is not enrolled in {course_code}.")
        return

    student.add_grade(course_code, grade)
    print(f"Grade {grade} added for {student.name} in {courses[course_code].course_name}.")

def display_student_details(students):
    student_id = input("Enter Student ID: ").strip()
    if student_id not in students:
        print(f"Student ID {student_id} does not exist.")
        return
    students[student_id].display_student_info()

def display_course_details(courses):
    course_code = input("Enter Course Code: ").strip()
    if course_code not in courses:
        print(f"Course Code {course_code} does not exist.")
        return
    courses[course_code].display_course_info()
