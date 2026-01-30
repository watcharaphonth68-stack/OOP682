class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"{self.name} is {self.age} years old."
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    pass

def main():
    my_dog = dog("Buddy", 3)
    print(my_dog)
    your_dog = dog("Max", 5)
    print(your_dog.info())

if __name__ == "__main__":
    main()
