def is_strong_password(password):
    """Checks if password meets enterprise security standards."""
    # 1. Minimum length check
    if len(password) < 8:
        return False
        
    # 2. Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False
        
    # 3. Check for lowercase letters
    if not any(char.islower() for char in password):
        return False
        
    # 4. Check for uppercase letters
    if not any(char.isupper() for char in password):
        return False
        
    # 5. Check for special characters
    special_chars = '!@#$%^&*()_+'
    if not any(char in special_chars for char in password):
        return False
        
    return True

# --- Testing the function ---
print("WeakPwd:", is_strong_password("WeakPwd"))       # Output: False
print("Str0ngPwd!:", is_strong_password("Str0ngPwd!")) # Output: True

import re

def is_valid_email(email):
    """Validates email format using regular expressions."""
    # Pattern explanation:
    # ^[a-zA-Z0-9_.+-]+  -> Starts with alphanumeric chars, dots, or underscores
    # @                  -> Requires an '@' symbol
    # [a-zA-Z0-9-]+      -> Domain name (e.g., 'gmail' or 'company')
    # \.[a-zA-Z0-9-.]+$  -> Top-level domain (e.g., '.com', '.co.uk')
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # re.match returns a Match object if valid, or None if invalid
    return re.match(pattern, email) is not None

# --- Testing the function ---
print("Valid email:", is_valid_email("admin@domain.com")) # Output: True
print("Invalid email:", is_valid_email("user@.com"))      # Output: False


def calculate_total_cost(cart):
    """Calculates the total monetary value of items in a shopping cart."""
    total_cost = 0.0
    
    for item in cart:
        # Access individual dictionary keys for each entry
        price = item['price']
        quantity = item['quantity']
        
        total_cost += price * quantity
        
    return total_cost

# --- Testing the function ---
cart_data = [
    {'name': 'Apple', 'price': 0.5, 'quantity': 4},
    {'name': 'Banana', 'price': 0.3, 'quantity': 6},
    {'name': 'Orange', 'price': 0.7, 'quantity': 3}
]

total = calculate_total_cost(cart_data)
print("Total Cost:", round(total, 2))  # Output: 5.9


def count_word_frequency(file_path):
    """Reads a file line-by-line and returns a word frequency count dictionary."""
    word_count = {}
    
    # Context manager automatically handles file opening and closing
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Clean punctuation and normalize case
                word = word.lower().strip('.,!?;:"\'')
                
                # dict.get(word, 0) fetches current count or 0 if key doesn't exist
                word_count[word] = word_count.get(word, 0) + 1
                
    return word_count

# --- Sample Usage ---
# If sample.txt contains: "Hello world! Hello Python."
# Output: {'hello': 2, 'world': 1, 'python': 1}
filepath='sample.txt'
word_frequency=count_word_frequency(filepath)
print(word_frequency)


def convert_temperature(temp, unit):
    """Converts temperatures between Celsius (C) and Fahrenheit (F)."""
    if unit == 'C':
        # Celsius to Fahrenheit formula
        return (temp * 9/5) + 32
    elif unit == 'F':
        # Fahrenheit to Celsius formula
        return (temp - 32) * 5/9
    else:
        # Fallback for unsupported unit parameters
        return None

# --- Testing the function ---
print("25°C to F:", convert_temperature(25, 'C')) # Output: 77.0
print("77°F to C:", convert_temperature(77, 'F')) # Output: 25.0


def is_palindrome(text):
    """Checks if a string reads the same backward as forward, ignoring case and spaces."""
    # Convert to lowercase and strip spaces
    cleaned_text = text.lower().replace(" ", "")
    
    # Compare original string with reversed string slice
    return cleaned_text == cleaned_text[::-1]

# --- Testing the function ---
print("Palindrome test 1:", is_palindrome("A man a plan a canal Panama")) # Output: True
print("Palindrome test 2:", is_palindrome("Python"))                      # Output: False

def factorial(n):
    """Calculates n! using recursion."""
    # Base Case: prevents infinite recursion loops
    if n == 0:
        return 1
    else:
        # Recursive Step: function calls itself with (n - 1)
        return n * factorial(n - 1)

# --- Execution Breakdown for factorial(4) ---
# 4 * factorial(3)
# 4 * (3 * factorial(2))
# 4 * (3 * (2 * factorial(1)))
# 4 * (3 * (2 * (1 * factorial(0))))
# 4 * 3 * 2 * 1 * 1 = 24

print("Factorial of 6:", factorial(6)) # Output: 720