import json
from models.student import Student
from models.course import Course

DATA_FILE_JSON = "data/data.json"
DATA_FILE_TXT = "data/data.txt"

def save_data(students, courses):
    # --- Save to JSON ---
    data = {
        "students": {sid: student.to_dict() for sid, student in students.items()},
        "courses": {cid: course.to_dict() for cid, course in courses.items()}
    }
    with open(DATA_FILE_JSON, "w") as f:
        json.dump(data, f, indent=4)
    print(" JSON file saved successfully.")

    # --- Save to TXT ---
    with open(DATA_FILE_TXT, "w") as f:
        f.write("===== STUDENTS =====\n")
        for sid, student in students.items():
            f.write(f"ID: {sid}, Name: {student.name}, Age: {student.age}, Address: {student.address}\n")

        f.write("\n===== COURSES =====\n")
        for cid, course in courses.items():
            f.write(f"ID: {cid}, Title: {course.title}, Instructor: {course.instructor}\n")
    print(" TXT file saved successfully.")

def load_data():
    try:
        with open(DATA_FILE_JSON, "r") as f:
            data = json.load(f)

        students = {sid: Student.from_dict(sdata) for sid, sdata in data["students"].items()}
        courses = {cid: Course.from_dict(cdata) for cid, cdata in data["courses"].items()}

        print(" Data loaded successfully from JSON.")
        return students, courses
    except FileNotFoundError:
        print(" No saved JSON data found. Starting fresh.")
        return {}, {}
