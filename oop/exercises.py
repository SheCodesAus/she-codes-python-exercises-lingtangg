from cmath import sqrt
# # 1
# class Book:

#     # properties of the Book object
#     def __init__(self, title, author, pages, current_page):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = current_page
#         self.bookmark = 1

#     # methods of the Book object 
#     def bookmark_page(self, page_number = None):
#         if page_number == None:
#             self.bookmark = self.current_page
#         else:
#             self.bookmark = page_number

#     # method takes in one argument -> direction which can be True or False (or anything else)
#     def turn_page(self, direction):
#         if direction and (self.current_page + 1) > self.pages:
#             self.current_page = 1
#         else:
#             if direction:
#                 self.current_page += 1
#             else:
#                 self.current_page -=1

#     def go_to_page(self, page):
#         self.current_page = page

#     def __str__(self):
#         return f"Title:{self.title}, Author:{self.author}, Pages:{self.pages}"

#     # determines the length of the Book object
#     def __len__(self):
#         return self.pages

# my_book = Book("A great book", "me", 198, 1)

# print(my_book)

# my_book.go_to_page(197)
# my_book.turn_page(True)
# print(my_book.current_page)

# # 2
# from turtle import width


# class Rectangle:

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return (self.width + self.height) * 2

#     def diagonal(self):
#         return "{:.2f}".format(sqrt(self.width ** 2 + self.height ** 2))

#     def is_square(self):
#         if self.width == self.height:
#             return "It is a square"
#         else:
#             return "It is not a square"

# rectangle = Rectangle(10, 5)

# print(rectangle.area())
# print(rectangle.perimeter())
# print(rectangle.diagonal())
# print(rectangle.is_square())

# 3 
class Vehicle:

    def __init__(self, make, model, colour, capacity, max_speed, fuel_tank, fuel_consumption, current_fuel):
        self.make = make
        self.model = model
        self.colour = colour
        self.capacity = capacity
        self.max_speed = max_speed
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.current_fuel = current_fuel

    def rev_engine(self):
        return "VRRRRMMM!"
    
    def km_driven(self, km):
        fuel_used = km * self.fuel_consumption / 100
        self.current_fuel = self.current_fuel - fuel_used

    def check_fuel(self):
        if self.current_fuel < 5:
            return f"You have {self.current_fuel}L of fuel or {self.current_fuel * self.fuel_consumption}km left. Go fill up!"
        else:
            return f"You have {self.current_fuel}L of fuel or {self.current_fuel * self.fuel_consumption}km left."

    def __str__(self):
        return f"{self.colour} {self.make} {self.model} with a seating capacity of {self.capacity} and a maximum speed of {self.max_speed}km/h. It has a {self.fuel_tank}L fuel tank and consumes {self.fuel_consumption}L/100km. It currently has {self.current_fuel}L of fuel left."

car = Vehicle("Toyota", "Yaris Cross", "Grey", 5, 200, 60, 5, 40)

print(car)
car.km_driven(100)
print(car.check_fuel())