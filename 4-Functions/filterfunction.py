scores = [45,82,67,90,55,74]
# "Keep 's' if 's >= 70' is True"

passing_score = list(filter(lambda s:s>=70,scores))
print(passing_score)
# Output: [82, 90, 74]

words = ["python", "go", "java", "c", "javascript"]
# Keep only words with more than 3 letters
long_words = list(filter(lambda w:len(w)>3,words))

print(long_words)
# Output: ['python', 'java', 'javascript']

users = [
    {"username": "alex", "is_active": True},
    {"username": "sam", "is_active": False},
    {"username": "jordan", "is_active": True}
]

# Keep only users where 'is_active' is True
active_users = list(filter(lambda u:u["is_active"],users))
print(active_users)
# Output: [{'username': 'alex', 'is_active': True}, {'username': 'jordan', 'is_active': True}]

mixed_data = ["hello","",0,"world",None,False,42]
# Remove all empty strings, zeros, and None values automatically
clean_data = list(filter(None,mixed_data))

print(clean_data)
# Output: ['hello', 'world', 42]