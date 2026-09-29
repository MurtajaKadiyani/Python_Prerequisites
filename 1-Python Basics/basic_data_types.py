# Create variables holding strings
greeting = "Hello, World!"
favourite_letter = 'A'

# Strings can also hold numbers, but they act like text, not math!
fake_number = "100"
print(greeting)

# Create variables holding integers
apples_in_basket = 12
temperature_celsius = -5

# Python can do math with integers
total_apples = apples_in_basket + 3
print(total_apples) # This prints 15

# Create variables holding floats
coffee_price = 4.99
pi = 3.14159    

# You can add ints and floats together safely
total_cost = coffee_price + 1
print(total_cost) # This prints 5.99

# Create boolean variables
is_raining = True
is_sunny = False

# This is often used in logic
if is_raining:
    print("Don't forget your umbrella!")

mystery_variable = "45.5"
another_mystery = 45.5

# Let's print the TYPES of these variables to the terminal
print(type(mystery_variable))  # This will print <class 'str'>
print(type(another_mystery))    # This will print <class 'float'>

age = 25
# We wrap 'age' in str() to temporarily turn the number 25 into the text "25"
message = "I am " + str(age) + " years old."
print(message)  # This will print: I am 25 years old.