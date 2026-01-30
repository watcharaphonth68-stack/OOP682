from models.student import student
from models.classroom import Classroom


oop = Classroom("oop")
oop.add_student(student(1,"a", 20 , "soo1"))
print(f"name={oop.name} registered {len(oop)}")
oop.add_student(student(2,"b", 21 , "soo3"))
print(len(oop))
print("students in the class:")
for i in range(len(oop)):
    print(oop[i])