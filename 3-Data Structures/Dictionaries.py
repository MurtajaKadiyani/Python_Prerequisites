# Creating a user profile dictionary
user = {
    "username": "alex99",
    "email": "alex@example.com",
    "age": 25,
    "is_active": True
}

# 1. Accessing values using square brackets
print("Username:", user["username"])
print("Email:", user["email"])

# 2. Accessing values safely using .get()
# If a key doesn't exist, square brackets give a KeyError!
# .get() returns None (or a custom fallback message) instead of crashing.
phone = user.get("phone", "Phone number not provided")
print("Phone:", phone)

user = {"name": "Sara", "score": 100}

# Add a new key-value pair
user["role"] = "admin"

# Update an existing key
user["score"] = 150

# Delete a key-value pair using pop()
removed_role = user.pop("role")

print("Updated Dictionary:", user)
print("Removed Role:", removed_role)

inventory = {"apples": 10, "bananas": 25, "oranges": 15}

# Loop over keys and values together
for item, count in inventory.items():
    print(f"We have {count} {item} in stock.")

# Loop over keys only
for item in inventory.keys():
    print(f"Item name:", item)

# Loop over values only
total_items = sum(inventory.values())
print("Total Items:", total_items)

# Suppose we have item prices in dollars and want to convert them to euros (rate: 0.9)
prices_usd = {"laptop": 1000, "mouse": 25, "monitor": 200}

# Create a new dictionary with converted prices for items over $30
prices_eur = {item: price * 0.9 for item, price in prices_usd.items() if price > 30}
print("EUR Prices:", prices_eur)
# Output: EUR Prices: {'laptop': 900.0, 'monitor': 180.0}


