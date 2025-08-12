class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []  # list of student IDs

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)

    def display_course_info(self):
        print("Course Information:")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        if self.students:
            print("Enrolled Students: " + ", ".join(self.students))
        else:
            print("Enrolled Students: None")

    def to_dict(self):
        return {
            "course_name": self.course_name,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "students": self.students
        }

    @classmethod
    def from_dict(cls, data):
        course = cls(data["course_name"], data["course_code"], data["instructor"])
        course.students = data.get("students", [])
        return course
