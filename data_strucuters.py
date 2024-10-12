# EX1:
# a. Define a list with 3 elements.
# b. Is the list an ordered data structure? Why or why not?
# c. Access the second element from the list and display it.
# d. Display the length of the list.

list = [1, 2, 3]
second_element = list[1]
print(second_element)
lenght = len(list)
print(lenght)


# EX2:
# a. Define a list called favorite_movies, with at least 3 elements.
# b. Reverse the list using slicing (as with strings).
# c. Using an if statement, check if the list is empty or not, and display an appropriate message for each case.

favorite_movies = ["Terminator", "Matrix", "World"]
reverse_movies = favorite_movies[::-1]
print(reverse_movies)
if favorite_movies:
    print("The list is not empty: ", favorite_movies)
else:
    print("The list is empty")

# EX3: Given the data structure digits = [0, 6, 3, 4, 1, 2, 5, 7, 8].
# a. Check the type of the given data structure.
# b. Using list methods, sort the list digits.
# c. Check if 9 is in the digits list. Display an appropriate message.

digits = [0, 6, 3, 4, 1, 2, 5, 7, 8]
print(type(digits))
digits.sort()
print(digits)
if 9 in digits:
    print("9 is in the digist list")
else:
    print("9 is missing")

# EX4: Define a list and explore helper methods of lists.
my_list = [10, 20, 30, 'apple', 'banana', True]
my_list.append(1000)
my_list.append("cherry")
my_list.insert(2, 'new')
my_list.remove('apple')
item = my_list.pop()
print(item)
index_of_banana = my_list.index('banana')
print(index_of_banana)
count_of_30 = my_list.count(30)
print(count_of_30)
my_list.reverse()
print(my_list)
my_list.extend(['mango'])
print(my_list)
my_list.clear()
print(my_list)
# EX5: Given the set: my_set = {1, 2, 3, 4}.
# a. Add the number 5 to the set.
# b. Add the number 6 to the set.
# c. Add the number 1 to the set. What do you observe?
# d. Remove an element from the set using the remove() method.
# e. Remove an element from the set using the pop() method.
my_set = {1, 2, 3, 4}
my_set.add(5)
print(my_set)
my_set.add(6)
my_set.add(1)
print(my_set)
my_set.remove(3)
removed_element = my_set.pop()
print(removed_element)
print(my_set)


# EX6: Given the following data structure:
#location = (44.34, 12.456)
# a. Check the type of the data structure.
# b. Is this data structure ordered?
# c. Is this data structure mutable?
# d. Determine the length of the data structure.
# e. Save the second value into a variable.
#    Check if it is greater than 13, and display an appropriate message.
location = (44.34, 12.456)

print(type(location))
#b yes
#c no
length = len(location)
print(length)

second_value = location[1]
if second_value > 13:
    print("The second value is greater than 13.")
else:
    print("The second value is not greater than 13.")

# EX7:
# a. Define a dictionary, named student1, with the following keys:
# name, surname, age, year_of_study, university, GPA. Choose the values yourself.
# b. Display the length of the dictionary.
# c. Print the student's surname.
# d. Add a new key-value pair with the country where the student studies.
# e. Check if the dictionary contains the key 'city'.

student1 = {
    'name' : 'Nick',
    'surname' : 'John',
    'age' : 34,
    'year_of_study': 3,
    'university': 'Ardem University',
    'GPA': 4
}
print(len(student1))
print(student1['surname'])
student1['country'] = 'USA'
print(student1)
if 'city' in student1
    print("The key 'city' is in the dictionary.")
else:
    print("The key 'city' is not in the dictionary.")


# EX8:
# a. Read the following data from the user related to a new recipe: name, ingredients, preparation time.
# b. Save the data read in a dictionary.
# c. Update the recipe name, converting it to uppercase.
recipe_name = input("Enter the recipe name: ")
ingredients = input("Enter the ingredients: ")
preparation_time = input("Enter the preparation time: ")

recipe = {
    "name" : recipe_name,
    "ingredients": [ingredient.strip() for ingredient in ingredients.split(",")],
    "preparation_time" : preparation_time
}
recipe["name"] = recipe["name"].upper()
print(recipe)


# EX9:
# a. Given a dictionary with phone contacts:
contacts = {'Maria': '0722898956', 'Aurel': '0755342298'}
# b. Aurel has changed his phone number. Update it.
# c. You have obtained Mihai's phone number. Add it to the contacts.
# d. Maria has moved abroad and no longer has a phone number. Delete it.
# e. Check if you have Mihaela's phone number and display an appropriate message.

contacts["Aurel"] = '0799989777'
contacts["Mihai"] = '0323232332'
del contacts["Maria"]
if 'Mihaela' in contacts:
    message = "Mihaela's phone number is available."
else:
    message = "Mihaela's phone number is not available."
print(contacts)