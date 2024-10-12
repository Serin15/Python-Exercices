# EX1: Given the string prop3 = 'The concert will take place tomorrow.'
# a. Save the first word in a variable using slicing.
# b. Extract the first 3 characters from prop3.
# c. Display prop3 with the characters reversed.
from variables_data_type import discount

prop3 = 'The concert will take place tomorrow'
print(prop3[:1])
print(prop3[:3])
print(prop3[::-1])

# EX2: Given the variable prop1 = 'Andy is short for Andrew.'
# a. Display the first character.
# b. Display the 4th character.
# c. Display the last character.

prop1 = 'Andy is short for Andrew'
print(prop1[0])
print(prop1[:3])
print(prop1[-1])

# EX3: Given the string prop2 = 'The car is red.'
# Display the length of the string prop2.

prop2 = 'The car is red'
print(len(prop2))

# EX4: Given the string my_str = 'vacation'.
# a. Use the find() method to find the first index where the character 'a' appears.
# b. Use the count() method to find how many times the character 'a' appears in my_str.
# c. Use the capitalize() method to capitalize the first letter of the word.
# d. Use the upper() method to convert the word to uppercase.

my_str = 'vacantion'
first_index = my_str.find('a')
print("First index of 'a': ", first_index)
count_a = my_str.count('a')
print("Numbers of 'a' characters:", count_a)
capitalize_first_letter = my_str.capitalize()
print("Capitalize word:", capitalize_first_letter)
upper_word = my_str.upper()
print("Uppercase word:", upper_word)

# EX5: Explore the following string helper methods:
# a. endswith()
# b. index()
# c. lower()
# d. replace()
# e. strip()

example_str = " Hello, world! "
result = example_str.endswith("!")
print("Ends with '!' ", result)
# false because un have a space in our string
index_of_hello = example_str.index('Hello')
print("Index of hello:", index_of_hello)
lower_str = example_str.lower()
print("Lower string:", lower_str)
replaced_str = example_str.replace('world', 'New')
print("Replaced string:", replaced_str)
stripped_str = example_str.strip()
print("Stripped string:", stripped_str)

# EX6: Given two variables, a = 10, b = 2.
# Perform all arithmetic operations on the two variables using arithmetic operators.

a = 10
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# EX7: For each of the examples below, write the expected result in a comment,
# then uncomment the code for each example one by one, run them, and check the output.

# Example 1:
a = True
b = False
# print(not(a))
# print(not(b))

# Example 2:
a = True
b = False
# x = not(a)
# y = not(b)
# print(a or b)
# print(x or y)
# print(a or x)
# print(x or b)

# Example 3:
a = False
b = False
# x = not(a)
# y = not(b)
# print(a and b)
# print(a and x)
# print(y and b)
# print(x and y)

# EX8: Given the variable num = 12
# a. Check if the number is positive.
# b. Check if the number is greater than 5.
# c. Check if the number is less than 25.
# d. Check if the number is between 0 and 20.

num = 12
is_pozitive = num > 0
print(is_pozitive)
is_greater = num > 5
print(is_greater)
is_less = num < 25
print(is_less)
is_between = 0 < num < 20
print(is_between)

# EX9: Check if the age entered by the user is greater than 18 years old.

age = int(input("Enter you age: "))
if age > 18:
    print("You are older than 18 years old")
else:
    print("you are 18 or younger")


# EX10: Check if the price entered by the user is less than or equal to 100 dollars.

price = float(input("Please enter the price in dollars: "))
if price <= 100:
    print("The price is less or  equal to 100 dollars")
else:
    print("the price is bigger than 100 dollars")


# EX11:
# a. Read a number from the keyboard.
# b. Check if the number is even or odd, and display an appropriate message for each case.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")


# EX12:
# a. Read the average driving speed of the user from the keyboard.
# b. If the speed is 50 or below, display the message "Normal speed".
# c. If the speed is above 50, display the message "Speed exceeded".


speed = float(input("Enter your the average driving speed (km/h) : "))
if speed <= 50:
    print("Normal speed")
else:
    print("Speed exceeded")


# EX13: Read the user's age from the keyboard and display the age category they fall into.
# Consider these age categories:
# - Between 0-18 years old: minor
# - Between 18-65 years old: adult
# - Over 65 years old: senior

age = int(input("Insert your age: "))
if age >= 0 and age < 18:
    print("You are minor")
elif age >= 18 and age <= 65:
    print("You are adult")
elif age > 65:
    print("You are senior")
else:
    print("Invalid age entered")


# EX14: This week, supermarket X is offering customers a discount on the total shopping basket
# depending on the total cost of the shopping basket.
# The discount is applied as follows:
# - Total is between 100 and 200 lei -> 10% discount
# - Total is between 200 and 300 lei -> 15% discount
# - Total is between 300 and 400 lei -> 20% discount
# - Total is greater than 400 lei -> 30% discount.
# a. Read the total shopping basket value from the user.
# b. Display the price the user has to pay after the discount is applied.


total_cost = float(input("Enter the total cost of your shopping basket (in lei): "))

if 100 <= total_cost <= 200:
    discount = 0.10
elif 200 < total_cost <= 300:
    discount = 0.15
elif 300 < total_cost <= 400:
    discount = 0.20
elif total_cost > 400:
    discount = 0.30
else:
    discount = 0.0

final_price = total_cost - (total_cost * discount)
print(f"The final price after discout is applied:{final_price:.2f} lei")