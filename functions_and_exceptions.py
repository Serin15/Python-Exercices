# EX1: Define a function that prints, one by one, the first 10 numbers (1 to 10).
def first_10_numbers():
    for number in range(1, 11):
        print(number)
first_10_numbers()



# EX2: Write a function that iterates through a given list of numbers and
# displays the message 'It is even' for even numbers and 'It is odd' for odd numbers.
# If the list contains an element that is not an integer,
# display a message to the user and then skip that element.
# (Use the built-in function isinstance() to check if the current element is an int or not.)

def check_even_odd(numbers):
    for number in numbers:
        if isinstance(number, int):
            if number % 2 == 0:
                print(f'{number} - It is even')
            else:
                print(f'{number} - It is odd')
        else:
            print(f'Warning: {number} is not an integer, skipping it.')

numbers_list = [1, 2, 3, 4, 5, 6, 'seven', 8.0, 9, None]
check_even_odd(numbers_list)


# EX3: Write a function that calculates the square of a number.
# Display the result.
def calculate_square(number):
    square = number ** 2
    print(f"The square of {number} is {square}")
calculate_square(2)



# EX4: Write a function that calculates the division between two numbers.
# Display the result.
def calculate_division(numerator, denominator):
    if denominator == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = numerator / denominator
        print(f'The result of {numerator} divided by {denominator} is {result}')

calculate_division(10, 2)


# EX5: Write a function that calculates the multiplication between two numbers.
# Display the result.

def calculate_multiplication(num1, num2):
    result = num1 * num2
    print(f'The result of {num1} multiplied by {num2} is {result}')

calculate_multiplication(5, 3)

# EX6: Rewrite the function from exercise 3 so that it returns the result.

def calculate_square(number):
    square = number ** 2  #
    return square


result = calculate_square(4)
print(f'The square of 4 is {result}')


# EX7: Rewrite the function from exercise 4 so that it returns the result.

def calculate_division(numerator, denominator):
    if denominator == 0:
        return "Error: Cannot divide by zero."
    else:
        result = numerator / denominator
        return result

result = calculate_division(10, 2)
print(f'The result of division is: {result}')

# EX8: Write a function that takes an integer as a parameter
# and returns True if the number is even, and False if the number is odd.

def is_even(number):
    return number % 2 == 0

print(is_even(2))
print(is_even(5))
