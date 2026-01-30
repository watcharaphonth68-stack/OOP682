from models.person import Person


class student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id
    def __str__(self):
        return f"PID: {self.pid}, Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"