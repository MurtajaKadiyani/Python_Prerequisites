from datetime import datetime, timedelta

# 1. Get current date and time
now = datetime.now()
print("Raw timestamp:", now)

# 2. Format dates into human-readable strings using strftime
# %Y = Year, %m = Month, %d = Day, %H = Hour, %M = Minute
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted time:", formatted_now)

# 3. Calculate future or past dates using timedelta
thirty_days_later = now + timedelta(days=30)
print("Date in 30 days:", thirty_days_later.strftime("%Y-%m-%d"))

import json
# Python Dictionary
user_data = {
    "Username": "coder_alex",
    "is_admin": True,
    "permission": ["read", "write"]
}

# 1. Serialize: Convert Python Dictionary -> JSON String (json.dumps)
json_string = json.dumps(user_data,indent=4)
print("JSON Output:\n", json_string)

# 2. Deserialize: Convert JSON String -> Python Dictionary (json.loads)
raw_json = '{"status": "success", "code":200}'
parsed_dict = json.loads(raw_json)
print("Status Code:", parsed_dict["code"]) # Access like a standard dict

from pathlib import Path

# Create a Path object pointing to a file
file_path = Path("sample_data.txt")

# 1. Check if a file or directory exists
print("File exists?", file_path.exists())

# 2. Get file details
print("File extension:", file_path.suffix)
print("Parent Folder:", file_path.parent.absolute())

# 3. Quickly write and read text files without manually opening/closing
file_path.write_text("Hello from pathlib!")
content = file_path.read_text()
print("File Content:", content)

from collections import Counter
# Count frequency of items in a list instantly
fruit_list = ["apple", "banana", "apple", "orange", "banana", "apple"]

fruit_counts = Counter(fruit_list)
print("Counter:", fruit_counts)
# Output: Counts: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Get the single most common item
print("Most frequent:", fruit_counts.most_common(1))
# Output: [('apple', 3)]

import math
import random

# Math operations
print("Square root of 64:", math.sqrt(64))
print("Ceiling (round up):", math.ceil(4.2)) # Output: 5

# Random operations
options = ["Red", "Green", "Blue", "Yellow"]
selected_color = random.choice(options)
print("Random Color:", selected_color)

random_number = random.randint(100, 999)
print("Random ID:", random_number)
