class car:
    def __init__(self, brand, fuel=100, speed=0):
        self.brand = brand
        self.fuel = fuel
        self.speed = speed
        pass

    def accelerate(self, amount):
        """
        Calculates fuel needed and accelerates if possible.

        Parameters:
        amount (int): The increase in speed.
        """
        fuel_needed = 0.5 * amount
        
        if self.fuel < fuel_needed:
            # What happens if we don't have enough fuel?
            print("Not enough fuel.")
        else:
            # What happens if we DO have enough fuel? (Your new code goes here!)
            self.speed += amount
            self.fuel -= fuel_needed
            print(f"The {self.brand} accelerates to {self.speed} km/h and leaves {self.fuel} litres of fuel in the tank.")

    def brake(self):
        self.speed = max(0, self.speed - 20)
        print(f"The {self.brand} slows down to {self.speed}km/h.")

    def refuel(self, amount):
        self.fuel += amount
        print(f"The {self.brand} refuels to {self.fuel} litres.")

car1 = car ("Mercedes", 100, 0)
car2 = car ("Lamborghini", 100, 0)

car1.accelerate(20, 5.4)
car1.brake()
car1.refuel(10)

car2.accelerate(30, 11.32)
car2.brake()
car2.refuel(11.654)