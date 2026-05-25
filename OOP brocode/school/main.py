from parent import *

def main():
    student = Student("Blake")
    student1= Student(input("Enter student name: "))
    teacher = Teacher("Mr Tareq")

    student1.submit_assignment()

    teacher.grade(student1)
    student.view_report()
    grades = Teacher.load_grades()

    for g in grades:
        print(f"{g['name']} | Mark: {g['mark']} | Feedback: {g['feedback']}")


if __name__ == "__main__":
    main()
