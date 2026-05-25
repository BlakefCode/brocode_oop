import csv

class Person:
    def __init__(self, name, classroom=None):
        self.name = name
        self.Classroom = classroom

    def enter_room(self, room):
        self.Classroom = room
        print(f"{self.name} has entered room {room.room_number}")


class Classroom:
    def __init__(self, room_number):
        self.room_number = room_number


class Notebook:
    def write_notes(self):
        print("Writing notes in book......")


class Report:
    def __init__(self, content):
        self.content = content

    def create(self):
        print("Creating report....")

    def get_summary(self):
        return self.content


class Canvas:
    def __init__(self):
        self.marks = {}

    def store_submission(self, student_name, mark):
        self.marks[student_name] = mark
        print(f"Stored submission for {student_name} in Canvas.")


class Edumate:
    def __init__(self):
        self.marks = {}

    def generate_report(self, student_name, mark):
        self.marks[student_name] = mark
        print(f"Marked and stored results for {student_name} in Edumate.")


#---------------------Teacher----------------#

class Teacher(Person):
    def __init__(self, name, classroom=None):
        super().__init__(name, classroom)
        self.canvas = Canvas()
        self.edumate = Edumate()

    def teach(self):
        if self.Classroom:
            print(f"{self.name} is teaching in {self.Classroom.room_number}")

    def save_grade(student_name, mark, feedback, filename="grades.csv"):
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_name, mark, feedback])

    def load_grades(filename="grades.csv"):
        grades = []
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if len(row) == 3:
                        name, mark, feedback = row
                        grades.append({
                            "name": name,
                            "mark": int(mark),
                            "feedback": feedback
                        })

        except FileNotFoundError:
            print("No grades file found.")
            return []
        return grades

    def grade(self, student):
        print(f"{self.name} is grading assignments")

        feedback = input(f"Grade {student.name}'s assignment and give feedback: ")
        mark = int(input("Enter mark: "))

        student.report = Report(feedback)
        student.graded_by = self.name

        self.canvas.store_submission(student.name, mark)
        self.edumate.generate_report(student.name, mark)

        Teacher.save_grade(student.name, mark, feedback)


#--------------------Student-----------------#

class Student(Person):
    def __init__(self, name, classroom=None):
        super().__init__(name, classroom)
        self.notebook = Notebook()
        self.report = None
        self.graded_by = None

    def study(self):
        if self.Classroom:
            print(f"{self.name} is studying in {self.Classroom.room_number}")
            self.notebook.write_notes()

    def submit_assignment(self):
        print(f"{self.name} is submitting assignments")

    def view_report(self):
        if self.report:
            print(f"{self.name}'s report: {self.report.get_summary()} graded by: {self.graded_by}")
        else:
            print("No report available.")