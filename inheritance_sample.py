from models.person import Person
from models.student import student 
from models.staff import staff


person1 = Person(1234567890, "John", 30)
student1 = student(12345678901, "Alice", 20, "S1001")
staff1 = staff(2345678912, "Bob", 35, "ST2001")
print(f"Student: {student1.name}, Age: {student1.age}, Student ID: {student1.student_id}")
print(f"Staff: {staff1.name}, Age: {staff1.age}, Staff ID: {staff1.staff_id}")
print(person1)
print(student1)
print(staff1)
def get_person_info(person):
    return isinstance(person, Person)
print(get_person_info(student1))
print(get_person_info(staff1))

# class EMployee:
#     pass
# manger = EMployee()
# get_person_info(manger)  # This will print False and return the name and age attributes will raise AttributeError