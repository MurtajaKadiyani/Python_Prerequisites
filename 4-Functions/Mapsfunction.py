prices = [10,20,30,40]

# "For every 'x' in prices, multiply it by 2"

doubled_prices = list(map(lambda x: x*2,prices))
print(doubled_prices)
# Output: [20, 40, 60, 80]

usernames = ["alice", "bob", "charlie"]
# "For every 'name' in usernames, run the .capitalize() method"
formatted_names = list(map(lambda name:name.capitalize(),usernames))
print(formatted_names)
# Output: ['Alice', 'Bob', 'Charlie']

shopping_cart = [
    {"item":"Apple", "price":1.50},
    {"item":"Banana", "price":0.75},
    {"item":"Milk", "price":2.99}
]

# "For every 'product' in the shopping cart, grab only the value connected to the 'item' key"
just_the_names = list(map(lambda product:product["item"],shopping_cart))
print(just_the_names)
# Output: ['Apple', 'Banana', 'Milk']