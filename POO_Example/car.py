from vehicule import Vehicle

class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, doors: int = 4):
        super().__init__(brand, model, year)
        self.__doors = doors
        
    @property
    def doors(self) -> int:
        """Get the number of doors"""
        return self.__doors
        
    @doors.setter
    def doors(self, doors: int):
        """Set the number of doors"""
        self.__doors = doors
        
    def honk(self):
        """Make the car honk"""
        print("Beep beep!")
        
    def __str__(self):
        """Return string representation of the car"""
        return f"{super().__str__()} with {self.__doors} doors"
