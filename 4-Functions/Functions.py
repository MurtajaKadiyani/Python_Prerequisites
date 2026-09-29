# 1. Defining the function
def greet():
    print("Hello! Welcome to the Python functions")

# 2. Calling (executing) the function
greet()
greet() # You can call it as many times as you want!

# 'name' and 'age' are parameters
def print_user_info(name, age):
    print(f"User Name: {name}")
    print(f"User Age: {age}")

# "Alice" and 28 are arguments
print_user_info("Alice", 28)

# Function using print (cannot be saved into a variable for later math)
def multiply_print(a, b):
    print(a * b)

# Function using return (gives the value back)
def multiple_return(a, b):
    return a * b
# Using the returned value
result = multiple_return(5, 4) # result now holds the number 20
final_score = result + 10  # We can continue doing math with it!
print("Final Score:", final_score) # Output: 30

# 'discount' defaults to 0 if not provided
def calculate_price(item_price, discount=0):
    final_price = item_price - discount
    return final_price

# Call without providing a discount
print("Price 1:", calculate_price(100))  # Output: 100

# Call providing a custom discount
print("Price 2:", calculate_price(100, 15)) # Output: 85

# *args example: Calculate total for Any number of items
def sum_everything(*numbers):
    # 'numbers' is a tuple containing all passed values
    return sum(numbers)

print(sum_everything(10,20))  # Output: 30
print(sum_everything(5,10,15,20,25))  # Output: 75

# **kwargs example: Handle flexible key-value properties
def build_profile(**user_details):
    # 'user_details' is a dictionary
    for key, value in user_details.items():
        print(f"{key.capitalize()}: {value}")

build_profile(username="coder123", status="Active", role="Developer")

global_variable = "I a visible everywhere!"

def my_function():
    local_variable = "I am inside the function!"
    print(local_variable)  # Works fine
    print(global_variable)  # Works fine

my_function()

# Uncommenting the line below causes a NameError!
# print(local_variable)

    