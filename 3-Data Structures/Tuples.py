# A standard tuple
coordinates = (34.05, -118.24)

# A tuple holding different data types
user_info = ("Alex", 28, True)

# Creating a tuple without parentheses (Python infers it!)
# This is called "tuple packing"
rgb_color = 255,128,0

print("Coordinates:", coordinates)
print("Color:", rgb_color)

not_a_tuple = ("apple") # Python reads this as a String
real_tuple = ("apples",) # Python reads this as a Tuple

server_config = ("192.168.1.1.", 8080, "Production")
# Accessing by index
ip_address = server_config[0]
port = server_config[1]

print(f"Connecting to {ip_address} on port {port}")

# Try running this code, and watch it fail!
settings = ("Dark Mode", "High Quality")
# ERROR: 'tuple' object does not support item assignment
# settings[0] = "Light Mode"

player_data = ("Wizard", 100, 50)

# Unpacking the tuple into three separate variables
character_class, health, magic = player_data

print("Class:", character_class)
print("Health:", health)
print("Magic:", magic)


