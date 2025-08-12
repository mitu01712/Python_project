from utils.menu import print_menu
from utils.operations import *
from utils.data_io import save_data, load_data

def main():
    students = {}
    courses = {}

    while True:
        print_menu()
        choice = input("Select Option: ").strip()

        if choice == "1":
            add_new_student(students)
        elif choice == "2":
            add_new_course(courses)
        elif choice == "3":
            enroll_student_in_course(students, courses)
        elif choice == "4":
            add_grade_for_student(students, courses)
        elif choice == "5":
            display_student_details(students)
        elif choice == "6":
            display_course_details(courses)
        elif choice == "7":
            save_data(students, courses)
        elif choice == "8":
            students, courses = load_data()
        elif choice == "0":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
