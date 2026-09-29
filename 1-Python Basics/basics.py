status = "running"
if status == "running":
    print("System is Operational.") # This line must be indented

repository_namee = "docker-local" #string
artifacts_count = 1250  #Integer
is_active = True  #Boolean

# Check if the repository has exceeded the artifacts threahold
if artifacts_count > 1000:
    print("Warning: Storage limit approaching")


# Setup our environment variables
environment = "Production"
scans_completed = 5

# Output the current state
print("Environment:", environment)

# Simple Conditinal Logic
if scans_completed > 0:
    print("Security scans are running succesfully.")
    print("Total scans:", scans_completed)
    