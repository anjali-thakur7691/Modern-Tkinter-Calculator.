import json
import os
from student import Student

class Studentmanager:
    FILE_NAME = "data.json"
    def __init__(self):
        self.students = []
        self.load_student()

    def load_students(self):
        if os.path.exists(self.FILE_NAME):

            with open(self.FILE_NAME,"r") as file:
                for item in data:
                    student = Student(
                        item["student_id"],
                        item["name"],
                        item["age"],
                        item["course"]
                    )
                self.students.append(student)

    def save_student(self):

        data = [] 
        for student in self.student:
            data.append(student.to_dict())
        with open(self.FILE_NAME,"w") as file:
            json.dump(data,file,indent=4)

    def add_students(self,student):
        self.students.append(student)
        self.save_student()

    def get_student(self):
        return self.students
    