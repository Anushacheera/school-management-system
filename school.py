import datetime

class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.courses = {}
        self.current_student_id = 0
        self.current_teacher_id = 0
        self.current_course_id = 0

    def add_student(self, name, age, grade):
        self.current_student_id += 1
        student_info = {
            "id": self.current_student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "enrollment_date": datetime.datetime.now()
        }
        self.students[self.current_student_id] = student_info
        return f"Student {name} added successfully with ID {self.current_student_id}."

    def add_teacher(self, name, subject):
        self.current_teacher_id += 1
        teacher_info = {
            "id": self.current_teacher_id,
            "name": name,
            "subject": subject,
            "hire_date": datetime.datetime.now()
        }
        self.teachers[self.current_teacher_id] = teacher_info
        return f"Teacher {name} added successfully with ID {self.current_teacher_id}."

    def add_course(self, course_name, teacher_id):
        if teacher_id in self.teachers:
            self.current_course_id += 1
            course_info = {
                "id": self.current_course_id,
                "course_name": course_name,
                "teacher_id": teacher_id,
                "creation_date": datetime.datetime.now()
            }
            self.courses[self.current_course_id] = course_info
            return f"Course {course_name} added successfully with ID {self.current_course_id}."
        else:
            return "Teacher ID not found."

    def view_students(self):
        if not self.students:
            print("No students found.")
        for student_id, student_info in self.students.items():
            print(f"ID: {student_id}, Name: {student_info['name']}, Age: {student_info['age']}, Grade: {student_info['grade']}, Enrollment Date: {student_info['enrollment_date']}")

    def view_teachers(self):
        if not self.teachers:
            print("No teachers found.")
        for teacher_id, teacher_info in self.teachers.items():
            print(f"ID: {teacher_id}, Name: {teacher_info['name']}, Subject: {teacher_info['subject']}, Hire Date: {teacher_info['hire_date']}")

    def view_courses(self):
        if not self.courses:
            print("No courses found.")
        for course_id, course_info in self.courses.items():
            teacher_name = self.teachers[course_info['teacher_id']]['name']
            print(f"ID: {course_id}, Course Name: {course_info['course_name']}, Teacher: {teacher_name}, Creation Date: {course_info['creation_date']}")


def main():
    sms = SchoolManagementSystem()

    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. View Students")
        print("5. View Teachers")
        print("6. View Courses")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            try:
                age = int(input("Enter student age: "))
            except ValueError:
                print("Invalid age. Must be a number.")
                continue
            grade = input("Enter student grade: ")
            print(sms.add_student(name, age, grade))

        elif choice == '2':
            name = input("Enter teacher name: ")
            subject = input("Enter teacher subject: ")
            print(sms.add_teacher(name, subject))

        elif choice == '3':
            course_name = input("Enter course name: ")
            try:
                teacher_id = int(input("Enter teacher ID: "))
            except ValueError:
                print("Invalid teacher ID.")
                continue
            print(sms.add_course(course_name, teacher_id))

        elif choice == '4':
            sms.view_students()

        elif choice == '5':
            sms.view_teachers()

        elif choice == '6':
            sms.view_courses()

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":

    main()
