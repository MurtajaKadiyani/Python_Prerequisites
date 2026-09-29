# We are assigning the text "John" to the variable named 'first_name'
first_name = "John"

# We are assigning the number 25 to the variable 'age'
age = 25

print(first_name)
print(age)

# --- VALID VARIABLES ---
score = 100  # Integer
player_1 = "Alice"  # String
_secret_code = 42 

# --- INVALID VARIABLES ---
#1st_player = "Bob"  # Invalid: starts with a number
#user name = "Charlie"  # Invalid: contains a space
#@special_char = "David"  # Invalid: starts with an @ symbol
#total-cost = 50  # Invalid: contains a hyphens

# Hard to read
highestscoreever = 999

# Better to use underscores for readability (snake_case)
highest_score_ever = 999

# First, let's put a number in the box
current_status = 50
print("Current Status:", current_status)

# Now, let's empty the box and put text in it instead
current_status = "Task Completed"
print("Current Status:", current_status)

# Assigning different values to different variables in one line
color, shape, quantity = "red", "circle", 10

print(color)
print(shape)
print(quantity)

# Assigning the same value to multiple variables in one line
x = y = z = 0
print(y) # this will print 0


