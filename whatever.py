# class Book:
    
#     def __init__(self, title, author, num_of_pages, price):
#         self.title = title
#         self.author = author
#         self.num_of_pages = num_of_pages
#         self.price = price
#         self.current_page = 0
#         print(f"Congrats on purchasing {title} by {author} for ${price:.2f}.")
    
#     def read(self, x):
#         self.current_page += x
#         if self.current_page >= self.num_of_pages:
#             print("Congratulations you've finished the book!")
#             self.current_page = 0
#         elif self.current_page < self.num_of_pages:
#             print(f"You are currently on {self.current_page}. There are {self.num_of_pages - self.current_page} pages left. ")
            
            
# book = Book("The Midnight Library", "Matt Haig", 288, 26.00)

# book.read(15)
# book.read(288)
# print(book.current_page)










# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def __str__(self):
#         return f"The animal you requested is named {self.name}, and it is a {self.species}."

#     def __repr__(self):
#         return f"<Animal | {self.name}, {self.species}>"

# animal1 = Animal("Leo", "lion")

# print(animal1)
# animal1








# class Car:
#     def __init__(self, color, model, make):
#         self.color = color
#         self.model = model
#         self.make = make

#     def drive(self):
#         print("The car is driving.")

#     def fill_up(self):
#         print("The car is filling up.")



# class Ford(Car):
#     def __init__(self, color, model):
#         super().__init__( color, model, "Ford")


# my_car = Ford('blue', 'Focus')

# print(my_car.make)
















from math import pi, pow

radius = 7

area = pi * radius **2

print(area)





a = 3
b = 4

c = (a**2 + b**2)**2

print(c)