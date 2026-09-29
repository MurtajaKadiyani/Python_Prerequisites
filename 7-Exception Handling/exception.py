def calculate_metrics(total_requests,failed_requests):
    try:
        # If total_requests is 0, this will cause a ZeroDivisionError
        failure_rate = failed_requests / total_requests
        print(f"Failure rate is {failure_rate * 100}%")

    except ZeroDivisionError:
        # This code ONLY runs if a ZeroDivisionError occurs
        print("[WARNING] Total request were 0. Cannot calculate failure rate.")

# --- Testing the function ---
calculate_metrics(100,5)  # Output: Failure rate is 5.0%
calculate_metrics(0,0)    # Output: [WARNING] Total requests were 0...

import json

def load_server_config(filepath):
    try:
        with open(filepath, 'r') as file:
            config = json.load(file)
            return config["server_port"]

    except FileNotFoundError:
        print(f"[ERROR] The file '{filepath}' does not exist. Falling back to default port.")
        return 8080
    except KeyError:
        print("[ERROR] File loaded, but 'server_port' is missing from the JSON.")
        return 8080
    except Exception as e:
        # The generic 'Exception' catches anything else we didn't predict
        # We assign it to 'e' so we can print the exact system error message
        print(f"[FATAl] An unexpected error Occured: {e}")
        return None

# --- Testing the function ---
# If config.json doesn't exist, it safely returns 8080 instead of crashing
port = load_server_config("missing_config.json")

def process_data_stream(stream_id):
    print(f"\n--- Starting Stream: {stream_id} ---")

    try:
        print("1. Opening connection to data stream...")
        # Simulating a crash if stream_id is a string instead of an integer
        result = 100 / stream_id

    except TypeError:
        print("2. [ERROR] Stream ID must be a number, not text.")
    except ZeroDivisionError:
        print("2. [ERROR] Stream ID cannot be zero.")

    else:
        # This only prints if try block executed flawlessly
        print(f"2. [SUCCESS] Data Processed: {result}")

    finally:
        # This prints whether it succeeded OR failed. 
        # It guarantees the connection is never left hanging open.
        print("3. Closing connection to data stream")

# --- Testing the flow ---
process_data_stream(5)  # Will succeed (runs try -> else -> finally)
process_data_stream("abc") # Will fail  (runs try -> except TypeError -> finally)