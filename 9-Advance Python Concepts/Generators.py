def simple_generator():
    print("-> Starting Generator")
    yield "First item"

    print("-> Resuming after first yield")
    yield "Second item"

    print("-> Resuming after second yield")
    yield "Third item"

# Initializing does NOT execute the function code yet
gen = simple_generator()

print(next(gen))   # Runs until first yield
print(next(gen))   # Resumes and runs until second yield

# def fetch_all_logs(count):
#     logs = []
#     for i in range(1, count + 1 ):
#         logs.append(f"LOG_ENTRY_{i}")  # Holds all 1,000,000 strings in RAM simultaneously

# # Consumes tens or hundreds of megabytes of RAM instantly
# all_logs = fetch_all_logs(1000000)

def stream_logs(count):
    for i in range(1, count + 1):
        yield f"LOG_ENTRY_{i}" # Generates 1 item at a time, emits it, and frees memory

# Takes almost 0 bytes of memory regardless of count
log_stream = stream_logs(1000000)

# Process items as they arrive
for log in log_stream:
    if "10" in log:
        print(f"Processing: {log}")
        break  # Stops processing early without ever generating the remaining 999,990 items!


def batch_generator(items, batch_size):
    """Yields successive batches of a specified size from a list or stream."""
    for i in range(0, len(items), batch_size):
        yield items[i : i + batch_size]

# --- Sample Data ---
artifacts = [
    "app-v1.0.tar.gz", "app-v1.1.tar.gz", "db-v2.0.tar.gz",
    "cache-v1.0.tar.gz", "auth-v3.2.tar.gz", "web-v1.0.tar.gz"
]

# Process artifacts in batches of 2
for batch in batch_generator(artifacts,batch_size=2):
    print(f"Uploading batch payload: {batch}")

# List comprehension (creates full list in RAM immediately)
list_comp = [x* 2 for x in range(1000000)]

# Generator expression (creates generator object, evaluates on demand)
gen_comp = (x * 2 for x in range(1000000))

print(type(gen_comp)) # Output: <class 'generator'>
print(next(gen_comp)) # Output: 0
print(next(gen_comp)) # Output: 2
