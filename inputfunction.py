# input function it prompts the user to input data
# input('what is your name: ?')
# creating an input variable
# name = input("What is your name")
# age = int(input('What is your age'))
#
# age = age + 1
# print(f'Hello {name}')
# print("Happy Birthday")
# print(f'You are {age} years old')
# calculating area of a rectangle//////////////////////////////////////////////////////
# length = float(input('What is the length of the rectangle?'))
# width = float(input('What is the width of the rectangle'))
# area = length * width
#
# print(f'length is {length}m')
# print(f'width is {width}m')
#
# print("Area of a rectangle is given by length * width")
# print(f'Area={length} * {width}')
# print(f"Area = {area}cm")
# Exercise 2 Shopping cart///////////////////////////////////////////////////////////
# item = input("What would you Like to shop?")
# price = int(input("Input Price"))
# quantity = int(input(f'How many {item}s do you want?'))
# total = int(price * quantity)
# print(f'Total price is {total}KSH')
# complex exercise 3
# Store items and their prices in a dictionary
Courses = {
    "Cyber Security": 600,
    "Software Engineering": 500,
    "Database Admin": 400
}
# Display the available items to the user
print('This is a list of the available')
for course, fees in Courses.items():
    print(f"{course.capitalize()}: {fees}$")

selected_item = input("What course would you like to take? ").lower()

# Normalize the course names to lowercase for comparison
normalized_courses = {course.lower(): fees for course, fees in Courses.items()}

# Check if the selected course is available (case-insensitive)
if selected_item in normalized_courses:
    price = normalized_courses[selected_item]
    quantity = int(input(f"How many {selected_item}s do you want? "))
    total = price * quantity
    print(f'Total price for {quantity} {selected_item}(s) is {total}$.')
else:
    print("Sorry, the course you selected is not available.")