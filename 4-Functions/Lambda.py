# --- The Standard Way ---
def add_ten_standard(num):
    return num + 10

print("Standard:", add_ten_standard(5)) # Output: 15

# --- The Lambda Way ---
# We assign it to a variable just so we can call it in this example
add_ten_lambda = lambda num: num + 10

print("Lamdba:" , add_ten_lambda(5)) # Output: 15

# A list of tuples containing (Name, Age)
users = [("Alice", 30), ("Bob", 19), ("Charlie", 25)]

# If we just do users.sort(), Python sorts alphabetically by Name.
# But what if we want to sort by Age? We use a lambda to tell Python to look at index 1!

users.sort(key= lambda user: user[1])
print("Sorted by age:", users)
# Output: Sorted by age: [('Bob', 19), ('Charlie', 25), ('Alice', 30)]

numbers = [1,2,3,4,5,6,7,8]
# We want to keep only the even numbers.
# The lambda function tests if a number divided by 2 has a remainder of 0.

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
# Output: Even numbers: [2, 4, 6, 8]