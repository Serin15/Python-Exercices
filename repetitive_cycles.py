# EX1: Given the number x = -5.
# Use a while loop to display negative numbers starting from -5.
# At the end, display a message that all negative numbers have been displayed.

x = -5
while x < 0:
    print(x)
    x += 1
print("All negative numbers have been displayed")

# EX2: Calculating the average
# We want to ask the user to input their exam grades.
# We will take input from the user until they enter -1.
# Based on the grades provided, we need to
# calculate the arithmetic average and display it.

total = 0
count = 0

while True:
    try:
        grade = float(input("Enter your grade (or -1 to finish): "))

        if grade == -1:
            break

        if grade < 0 or grade > 10:
            print("Grade must be between 0 and 10.")
            continue

        total += grade
        count += 1

    except ValueError:
        print("Please enter a valid number.")

if count > 0:
    average = total / count
    print("The average of the grades is:", average)
else:
    print("No grades were entered.")

# EX3: Display all even numbers up to 10.

for numbers in range(0, 11):
    if numbers % 2 == 0:
        print(numbers)


# EX4: Given the list:
vegetables = ['spinach', 'cucumbers', 'cauliflower', 'peppers']
# Display all the elements from the list by accessing them via their index.
vegetables = ['spinach', 'cucumbers', 'cauliflower', 'peppers']
for i in range(len(vegetables)):
    print(vegetables[i])


# EX5: Given the list:
products = [
    {
        'product name': 'Tomatoes',
        'price': 5
    },
    {
        'product name': 'Bread',
        'price': 8
    },
    {
        'product name': 'Milk',
        'price': 6
    },
    {
        'product name': 'Coffee'
    }
]
# Display all products that have a price greater than 5 lei.
for product in products:
    if 'price' in product and product['price'] > 5:
        print(product['product name'])

# EX6: Display the first even number in the range 1 - 10 (including both ends).
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
        break

# EX7: Given the list:
participants = ['Maria', 'Ionela', 'Marius', 'Paul']
# Using a loop, check if 'Marius' is in the list of participants.
# Once found, stop the loop.

for participant in participants:
    if participant == 'Marius':
        print("We found 'Marius' ")
        break

# EX8: Given the list:
numbers = [1, 2, 3, 4, 5, 6, 7]
# Display all elements from the list except for the numbers 3 and 5.

for number in numbers:
    if number not in [3, 5]:
        print(number)