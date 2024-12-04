class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0

    @property
    def brand(self) -> str:
        """Get the brand of the vehicle"""
        return self.__brand

    @brand.setter 
    def brand(self, brand: str):
        """Set the brand of the vehicle"""
        self.__brand = brand

    @property
    def model(self) -> str:
        """Get the model of the vehicle"""
        return self.__model

    @model.setter
    def model(self, model: str):
        """Set the model of the vehicle"""
        self.__model = model

    @property
    def year(self) -> int:
        """Get the year of the vehicle"""
        return self.__year

    @year.setter
    def year(self, year: int):
        """Set the year of the vehicle"""
        self.__year = year

    def roll(self, speed_increase: int):
        """Increase the speed of the vehicle"""
        self.__speed += speed_increase
        print(f"Rolling at {self.__speed} km/h")

    def brake(self, speed_decrease: int):
        """Decrease the speed of the vehicle"""
        self.__speed = max(0, self.__speed - speed_decrease)
        print(f"Braking to {self.__speed} km/h")

    def __str__(self):
        """Return string representation of the vehicle"""
        return f"{self.__year} {self.__brand} {self.__model}"