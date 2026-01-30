from models.person import Person

class Studen(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.studentid = student_id

    def __str__(self):
        return f"Student[{self.pid}, {self.name}, {self.age}, {self.studentid}]"