class Car:
    def __init__(self, brand, model, color, avg_consume, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.fuel = 0
        self.odometr = 0
        self.avg_consume = avg_consume

    def info_car(self):
        print(f"Brand: {self.brand}  Model {self.model} "
              f"Color: {self.color} Avg_consume {self.avg_consume} Price {self.price}")

    def ad_fuel(self, fuel):

        self.fuel = fuel
        print(self.fuel)
    def drive(self, km: int):
        if self.fuel == 0:
            print(f"There is't fuel, Pleas Add Fuel")
        if (self.fuel / self.avg_consume) * 100 < km:
            print(f"You heed more fuel")
        else:
            print("You arrived")
            self.odometr += km
            print(f"Your Odometr {self.odometr}")

tayota = Car("tayota", "camry70", "silver", 12, 18000)
tayota.info_car()
tayota.ad_fuel(16)
tayota.drive(100)