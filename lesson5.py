# class

# class Car:
#     color = "Grey"
#     wheels = 4
#
# car1 = Car()
# car1.color = 'Red'
# del car1.color
# car2 = Car()
# car2.number = "B394"
# print(car1.color)
# print(car2.__dict__)
# print(Car.__dict__)


class House:
    fundament = 'beton'

    def __init__(self,
                 count_window, count_room,
                 count_door, color_house):
        self.count_window = count_window
        self.count_room = count_room
        self.count_door = count_door
        self.color_house = color_house
        self.count_floor = 0


    def get_info(self):
        print(f"color: {self.color_house} ,floor: {self.count_floor} "
              f"windows: {self.count_window}, door: {self.count_door} "
              f"room: {self.count_room}")

    def build_floor(self):
        self.count_floor += 1
house_2 = House(15, 5, 5, "white")
house_19 = House(116, 100, 100, "black")
# print(house_2.__dict__)
# print(house_19.__dict__)
house_19.build_floor()

house_19.get_info()

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def info(self):
        print(f"Name Restauran:{self.restaurant_name} "
              f"Cuisine:{self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} open")
restaurant = Restaurant('Test', 'asian')
restaurant.info()
restaurant.open_restaurant()
