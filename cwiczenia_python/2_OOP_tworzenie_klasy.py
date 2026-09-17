class Cat:
    paw_count = 4


    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("Meow ~" + self.name)

    def add(self, a, b):
        return a + b


garfield = Cat("Garfield", 3, "orange")
felix = Cat("Felix", 5, "black")

garfield.speak()
felix.speak()

print("wiek Garfielda to: ", garfield.age)
garfield.age = 40
print("wiek Garfielda to teraz: ", garfield.age)

print(garfield.add(1, 5))
