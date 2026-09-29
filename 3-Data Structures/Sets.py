# Create a Set
active_users = {"Alice" , "Bob" , "Charlie"}

# Add a new user
active_users.add("Diana")

# Try to add a duplicate (Python ignores this)
active_users.add("Alice")

# Remove a user
active_users.remove("Bob")

print(active_users)
# The output order will be random! E.g., {'Charlie', 'Diana', 'Alice'}

python_students = {"Alice", "Bob" , "Charlie"}
java_students = {"Bob", "Charlie", "David"}

# 1. INTERSECTION (&)
# Who is taking BOTH Python and Java?
both = python_students.intersection(java_students)
# Shortcut syntax: python_students & java_students
print("Both:", both) # Output: {'Bob', 'Charlie'}

# 2. UNION (|)
# A complete list of ALL students, merging them without duplicates.
all_students = python_students.union(java_students)
# Shortcut syntax: python_students | java_students
print("All:", all_students) # Output: {'Alice', 'Bob', 'Charlie', 'David'}

# 3. DIFFERENCE (-)
# Who is taking Python, but NOT Java?
only_python = python_students.difference(java_students)
# Shortcut syntax: python_students - java_students
print("Only Python:", only_python) # Output: {'Alice'}