from animals import Dog, Cat
from car import Car

def main():
    # Create some animals
    dog = Dog("Rex", 3, "German Shepherd")
    cat = Cat("Whiskers", 2, "Orange")
    
    # Make the animals do things
    print("\n=== Animals ===")
    print(dog)
    dog.make_sound()
    print(cat) 
    cat.make_sound()
    
    # Create and use a car
    print("\n=== Vehicle ===")
    car = Car("Toyota", "Camry", 2020, 4)
    print(car)
    car.roll(50)
    car.honk()
    car.brake(20)

if __name__ == "__main__":
    main()
