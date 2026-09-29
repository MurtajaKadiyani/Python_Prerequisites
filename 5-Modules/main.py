# Save this inside main.py in the SAME folder
import calculator

# Call functions from your custom module
sum_result = calculator.add(10,5)
product_result = calculator.multiply(4,3)

print("Company:", calculator.COMPANY_NAME) # Output: Company: NAGARRO
print("Sum:", sum_result) # Output: Sum: 15
print("Product:", product_result) # Output: Product: 12

# Option 1: Import the whole module from the package
from utilities import string_helpers
result = string_helpers.make_uppercase("Hello world")
print(result) # Output: HELLO WORLD

# Option 2: Import a specific function directly
from utilities.string_helpers import make_uppercase
print(make_uppercase("python package")) # Output: PYTHON PACKAGE
