# Initialize cart
cart = ["apples", "milk","bread"]

# Add a new item to the end
cart.append("eggs")

# Check membership before adding duplicates
item_to_add = "milk"
if item_to_add in cart:
    print(f"'{item_to_add}' is already in the cart!")

# Remove a specific item by value
cart.remove("bread")
print("Final Cart:", cart)
# Output: Final Cart: ['apples', 'milk', 'eggs']

scores = [88, 92, 79, 65, 95, 71,100]
# Calculate summary statistics
total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)

# Extract only distinction-level scores (90+) using list comprehension
top_scores = [score for score in scores if score >= 90]
print(f"Average: {average:.1f}, | High: {highest} | Low: {lowest}")
print("Distinction Scores:", top_scores)

pending_tasks = ["Write Code", "Test script", "Deploy app"]
# Process tasks until the list is empty
while pending_tasks:
    current_task = pending_tasks.pop(0)  # pop(0) removes and returns the FIRST item in the list
    print(f"Processing task : {current_task} | Remaining tasks: {len(pending_tasks)}")

print("All tasks completed!")

raw_user_input  = "  python  , data strcuture ,   beginner   "

cleaned_tags = [tag.strip() for tag in raw_user_input.split(",")]
print("Cleaned List:", cleaned_tags)

# Reassemble the list into a clean display string
display_string = " | ".join(cleaned_tags)
print("Display String:", display_string)