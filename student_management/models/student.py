from .person import Person

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.courses = []  # course codes list
        self.grades = {}   # {course_code: grade}

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def add_grade(self, course_code, grade):
        if course_code in self.courses:
            self.grades[course_code] = grade

    def display_student_info(self):
        print("Student Information:")
        self.display_person_info()
        print(f"ID: {self.student_id}")
        if self.courses:
            enrolled_courses = ", ".join(self.courses)
            print(f"Enrolled Courses: {enrolled_courses}")
        else:
            print("Enrolled Courses: None")
        print(f"Grades: {self.grades if self.grades else '{}'}")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address,
            "student_id": self.student_id,
            "courses": self.courses,
            "grades": self.grades
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["name"], data["age"], data["address"], data["student_id"])
        student.courses = data.get("courses", [])
        student.grades = data.get("grades", {})
        return student
