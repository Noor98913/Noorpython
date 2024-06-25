The "Noor First Exercise.ipynb" file contains simple exercises for the basic information about Python language that we learned on the first day:

We discussed the following points:

1-Data Types:

Python has several built-in data types. Here are a few of the most common ones:

    Numeric Types: int, float, complex
    Text Type: str
    Sequence Types: list, tuple, range
    Mapping Type: dict
    Set Types: set
    Boolean Type: bool
    None Type: None

2-Arithmetic Operations

Python supports the following arithmetic operations:

    Addition: +
    Subtraction: -
    Multiplication: *
    Division: /
    Modulus: %
    Exponentiation: **
    Floor Division: //

3-String Operations

Python supports the following string operations:

    Concatenation: +
    Repetition: *
    Membership Test: in
    String Formatting: format()


Exersice1:
Complete the code to print out Hello Python! in a formatted string.

Code:
message = "Python"
Greeting = None
Greeting = f"Hello {message}!"
print(Greeting)

Outputs:
Hello Python!

Exersice2:
Correct the following code to:
1. Perform the arithmetic operation on a and b.
2. Perform concatenation on a and b.

Code:
a = 5
b = "10"

# perform addition expected output is 15
sum = a + int(b)
print(sum)

# perform concatenation expected output is 510
print((str(a) + b))

Outputs:
15
510
------------------------------
4-Sequence Types: list, tuple, range

Python has three sequence types:

    list: Ordered and changeable collection of items. Lists are defined by square brackets ([]).
    tuple: Ordered and unchangeable collection of items. Tuples are defined by parentheses (()).
    range: A sequence of numbers. Ranges are defined by the range() function.

5- Mapping Type: dict

Dictionaries are collections of items that are unordered, changeable, and indexed. Dictionaries are defined by curly brackets ({}) and consist of key-value pairs.

Exersice3:
Complete the code to extract and print out the domain name from the email address.

Code:
email = "python_dev@estarta.com"
# extract domain from email
domain = email[10: ]
print(domain)

Outputs:
@estarta.com

Exersice4:
Perform the following operations on the "Cars" list:
1. Add "Honda" to the list.
2. Replace the second element with "Ford".
3. Remove "Toyota" from the list.
4. Check if "Subaru" is in the list.

Code:
cars = ["Toyota", "Mercedes", "BMW", "Jeep"]

# add "Honda" to the list
cars.append("Honda")
# replace the second element with "Ford"
cars[1] = "Ford"
# remove Toyota from the list
cars.remove("Toyota")
print(cars)

# print True if Subaru is in the list else False
print("Subaru" in cars)

Outputs:
['Ford', 'BMW', 'Jeep', 'Honda']
False

Exersice5:
Complete the code to do the following:
1. Create a new dictionary with the following key-value pairs: "name": "Ahmad", "age": 25, "occupation": "doctor", "country": "Jordan"
2. Add a new key-value pair with "city": "Amman"
3. Update the occupation to "Surgeon"
4. Remove the "country" key-value pair from the dictionary.
5. print out the updated dictionary.

Code:
# complete the code to perform the operations listed above
person = {
  "name": "Ahmed",
  "age": 25,
  "occupation": "doctor",
  "country": "Jordan"
}
person["city"] = "Amman"
person["occupation"] = "Surgeon"
person.pop("country")
print(person)

Outputs:
{'name': 'Ahmed', 'age': 25, 'occupation': 'Surgeon', 'city': 'Amman'}
------------------------------
6- Set Types: set

Sets are unordered collections of unique items. Sets are defined by curly brackets ({}).

Exersice6:
Complete the folowing opertasions on the "numbers" set:
1. Check if 4 is in the set.
2. Add 5 to the set.
3. Remove 3 from the set.
4. Try to add a duplicate element to the set.
5. Create a new set that contains numbers from in the range of m+1 to m+10, where m is the maximum number in the "numbers" set.
6. Create a set that is the union of the two sets.

Code:

numbers = {2, 5, 16, 8, 7, 9, 3, 1}
# your code here
print(4 in numbers)
numbers.add(5)
numbers.remove(3)
numbers.add(7)

m = max(numbers)
new_set = set(range(m+1, m+11))
setunion = numbers.union(new_set)

print(numbers)
# print the union of the two sets

print(setunion)
#print(new_set)
print(new_set)

Outputs:
False
{1, 2, 5, 7, 8, 9, 16}
{1, 2, 5, 7, 8, 9, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}
{17, 18, 19, 20, 21, 22, 23, 24, 25, 26}
