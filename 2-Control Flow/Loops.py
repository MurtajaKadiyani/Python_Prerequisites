# Example 1: Loop 5 times (generates 0, 1, 2, 3, 4)
for i in range(5):
    print("Loop Iteration:",i)

# Example 2: Specify start and stop (generates 1, 2, 3, 4, 5)
for count in range(1,6):
    print("Counting:",count)

# Example 3: Loop over characters in a string
for letter in "Python":
    print("Letter:", letter)

countdown= 5

# Runs as long as 'countdown' is greater than 0
while countdown > 0:
    print("T-minus", countdown)
    countdown -= 1  # Subtracts 1 so the loop eventually stops

print("Blast off!")

# 'break' Example: Exit loop early
print("Break Example:")
for num in range(1,10):
    if num ==5:
        print("Reached 5, exiting loop!")
        break  # Exits the loop when num is 5
    print("Number:", num)

# 'continue' Example: Skip a specific item
print("Continue Example:")
for num in range(1,6):
    if num == 3:
        print("Skipping 3")
        continue # Moves to num = 4 without printing 3
    print("Number:", num)