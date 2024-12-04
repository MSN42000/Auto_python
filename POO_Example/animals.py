class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        """Make the animal's sound"""
        pass

    def __str__(self):
        """Return string representation of the animal"""
        return f"{self.name}, {self.age} years old"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        """Make the dog bark"""
        print("Woof woof!")

    def __str__(self):
        """Return string representation of the dog"""
        return f"{super().__str__()}, {self.breed} dog"


class Cat(Animal):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        """Make the cat meow"""
        print("Meow!")

    def __str__(self):
        """Return string representation of the cat"""
        return f"{super().__str__()}, {self.color} cat"

