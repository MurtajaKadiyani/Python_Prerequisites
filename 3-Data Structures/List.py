# Creating lists
temperatures = [72,74,76,79,81]
mixed_list = ["Alice", 72,True,3.14]

# 1. Accessing Items (Zero-Indexed)
# Python starts counting at 0, not 1!

print(temperatures[0]) # Output: 72
print(temperatures[2]) # Output: 76

# Negative indexing lets you count from the end backwards
print(temperatures[-1]) # Output: 81

# 2. Modifying Items
temperatures[0] = 70   # Changes the first item from 72 to 70
print(temperatures) # Output: [70, 74, 76, 79, 81]

# 3. Adding and Removing Items
temperatures.append(85) # Adds 85 to the end of the list
temperatures.pop(1) # Removes the item at index 1 (74)
temperatures.remove(79) # Removes the first occurrence of 79
print(temperatures) # Output: [70, 76, 81, 85]

numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)
print("Old Way:", doubled_numbers) # Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
# Look at how clean this is!
doubled_numbers = [num * 2 for num in numbers]
print("New Way:", doubled_numbers) # Output: [2, 4, 6, 8, 10]

raw_data = [1,2,3,4,5,6]
# Read this as: "Multiply by 10 for every num in raw_data, IF the num is even"
processed_data = [num * 10 for num in raw_data if num % 2 == 0]
print(processed_data) # Output: [20, 40, 60]