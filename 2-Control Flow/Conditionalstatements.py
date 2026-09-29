temperature = 35

print("Staring the program...")

# Python checks: Is 35 greater than 30? Yes (True).
if temperature > 30:
    print("Its a hot day")
    print("Drink plenty of water")

# This line is not indented, so it is outside the 'if' block.
# It runs regardless of what the temperature is.
print("Program Finished")

password_attempt = "wrongpassword"
correct_password = "Murtajapassword123"

if password_attempt == correct_password:
    print("Access granted")
else:
    # Because the strings don't match, the 'if' is False.
    # Therefore, the 'else' block executes.
    print("Access denied. Incorrect password.")


score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    # Because 85 is NOT >= 90, Python checks here.
    # 85 IS >= 80, so this block runs, and the rest is skipped.
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

