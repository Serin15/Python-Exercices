# EX1:
# a. Define an int variable called 'width'.
# b. Define a string variable called 'description'.
# c. Define 2 float variables called 'price' and 'discount'.
# d. Define a bool variable called 'initialized' with the value True.
# e. Print the variables defined in the previous points.

#a
width = 12
#b
description = "distance"
#c
price, discount = 12.2, 12.3
#d
initialized = True
#e
print("width", width, "description", description,  "price", price, "discount", discount, "initialized", initialized)


# EX2: Using a single line of code, define 2 int variables, both with the value 10.

price = amount = 10

# EX3: Using a single line of code, initialize/define two string variables with different values.

bike, motor = "left", "right"

# EX4: Define two string variables called 'name' and 'price'.
# Display a message in the console that contains both variables.
name = "John"
price2 = 2
print(f"My friend, {name}, has {price2} brothers!")

# EX5:
# a. Define two variables: name (string) and age (int).
# b. Using an f-string, display a sentence in the console that contains both variables.
name = "Andy"
age = 45
print(f"{name} is {45} years old")


# EX6:
# a. Define an int variable, display it in the console. Also display its type.
# b. Define a float variable, display it in the console. Also display its type.
# c. Define a string variable, display it in the console. Also display its type.
# d. Define a bool variable, display it in the console. Also display its type.

#a
my_int = 20
print("Integer value", my_int)
print("Type:", type(my_int))
#b
my_float = 15.5
print("Float value", my_float)
print("Type:", type(my_float))
#c
my_str = "strong"
print("String value", my_str)
print("Type:", type(my_str))
#d
my_bool = True
print("Boolean value", my_bool)
print("Type:", my_bool)

# EX7:
# a. Define an int variable. Display it in the console.
# b. Display the type of the variable defined in point a using the type() function.
# c. Convert the int variable from point a to a float and save the result in another variable.
# d. Display the type of the variable generated in point c.

#a
int = 15
print(int)
#b
print(type(int))
#c
float1 = float(int)
#d
print(type(float1))



# EX8:
# a. Define a string variable. Display it in the console.
# b. Display the type of the variable defined in point a using the type() function.
# c. Convert the variable from point a to an int and save the result in a new variable.
# Run the program. What do you notice?

# a.
my_str = "hello world"
print(my_str)

# b.
print(type(my_str))

# c.
print("We cannot convert a normal string (e.g., 'hello world') to int.")

# EX9: Read a product name from the keyboard. Save the result in a variable.
# Display a message that contains the saved variable.

name = input("Please enter the product name: ")
print(f"The product you entered is: {name}")



# EX10: Read a price from the keyboard. Force the user to enter the price as a decimal number.
# Save the result in a variable. Display a message that contains the saved variable.

# EX10: Read a price from the keyboard.
# Ensure that the user enters the price as a decimal number.

def get_price():
    while True:
        try:
            price1 = float(input("Insert a price (decimal number): "))
            return price1
        except ValueError:
            print("The input is invalid. PLease enter a decimal number")

price1 = get_price()

print(f"Price: {price1:.2f} $")

