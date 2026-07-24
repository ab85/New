# print ("Hello, World!")
# name = input("What is your name? ")
# print(f"Hello, {name}!")

# age = int(input("What is your age? "))
# years_remaining = 100 - age
# print(f"You have {years_remaining} years until 100!")

# print("Hello Anik")

# name = "Anik"
# print(name)
# age = 25
# print(age)

# height = 5.7
# print(height)

# is_raining = True
# print(is_raining)

# is_student = False
# print(is_student)

# print("Learning Python is fun!")
# print(name)
# print("I am", age, "years old")
# print(f"My height is {height} feet")

# age = int(input("What is your age? "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# score = int(input("What is your score?"))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# else:
#     print("Grade: D")

# name = input("What is your name?")
# print(f"hello, {name}!")
# age = int(input("What is your age? "))
# hours_worked = int(input("How many hours do you work per week? "))

# if age >= 18:
#     print("Legal adult - can vote")

# else:
#     print("Not yet 18")

# if hours_worked > 40:
#     print("Overtime pay")

# elif hours_worked == 40:
#     print("Regular pay")

# else:
#     print("Part-time work")

# for i in range(5):
#     print(i)

# fruits = ["apple", "bana", "mango"]
# for fruit in fruits:
#     print(fruit)

# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")  # prints 0: apple, 1: banana, etc

# for count in range(5):
#     print(count)

# grades = [85, 92, 78, 95, 88]
# for grade in grades:
#     if grade >= 90:
#         print(f"Grade {grade}: Excellent!")
#     else:
#         print(f"Grade {grade}: Good")

# grades = int(input("Enter your Grade : "))
# if grades >= 90:
#     print("Excellent")
# else:
#     print("Good")

# cart = [5.99, 12.50, 3.25, 8.00]
# total = 0
# for price in cart:
#     total += price
# print(f"Total: ${total}")

cart = int(input("Enter the number of items in your cart: "))
total = 0

for i in range(cart):
    price = float(input(f"Enter the price of item {i + 1}: "))
    total += price

print(f"Total: ${total:.2f}")