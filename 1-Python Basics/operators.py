x = 15
y = 4

print("Addition:", x + y)        # Addition: 19
print("Floor Division:", x // y)  # Floor Division: 3
print("Modulo (Remainder):", x % y)  # Modulo (Remainder): 3

score = 10
# The player finds a health potion! Let's add 5 to their score.
score += 5  # This is shorthand for score = score + 5
print("New score:", score)  # New score: 15

# The player takes damage!
score -= 2
print("Score after damage:", score)  # Score after damage: 13

my_age = 25
legal_drinking_age = 21

print("Am I old enough to drink?", my_age >= legal_drinking_age)  # True

password_attempt = "password123"
correct_password = "SecurePassword!"

print("Is the password correct?", password_attempt == correct_password)  # False

has_ticket = True
has_id = False
# Using AND: Both must be True
can_enter_club = has_ticket and has_id
print("Can I enter the club?", can_enter_club)  # False

# Using OR: Only one needs to be True
will_eat_pizza = True
will_eat_salad = False
print("Will eat Dinner?", will_eat_pizza or will_eat_salad)  # True
