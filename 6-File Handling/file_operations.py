# 1. Open the file in 'w' (write) mode
with open('repo_config.txt', 'w') as file:
    # 2. Use the .write() method to add text
    file.write("repository_name=docker-prod-local\n")
    file.write("retention_days=90\n")
    file.write("scan_on_push=true\n")

print("Configuration file generated succesfully")

# Open the file in 'r' (read) mode
with open('repo_config.txt', 'r') as file:
    # .readlines() grabs every line and puts it into a list
    lines = file.readlines()

print("Raw extracted lines:", lines)

# Often, you will want to loop through and clean up the data
print("\nCleaned Configuration:")

for line in lines:
    # .strip() removes the invisible '\n' newline characters and extra spaces
    clean_line = line.strip()
    print(f"- {clean_line}")

from datetime import datetime

def log_security_event(event_message):
    """Appends a timestamped event to an ongoing audit log."""

    # Open the file in 'a' (append) mode
    with open('security_audit.log', 'a') as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append the new message to the bottom of the file
        log_file.write(f"[{timestamp}] {event_message}\n")

# Simulate a few events occurring
log_security_event("Started vulnerability scan on helm-charts-core")
log_security_event("CRITICAL: Outdated NGINX controller detected")
log_security_event("Scan completed successfully")

print("Events appended tp security_audit.log")

import json

# Python Dictionary representing a server payload
migration_status = {
    "server_cluster": "aks-cluster-01",
    "status": "completed",
    "migrated_workloads": 45
}

# 1. WRITING JSON TO A FILE
with open('migration_report.json', 'w') as json_file:
    # json.dump() translates the Python dictionary into a JSON file
    # indent=4 formats it nicely so it is easy for humans to read
    json.dump(migration_status, json_file, indent=4)

# 2. READING JSON FROM A FILE
with open('migration_report.json', 'r') as json_file:
    # json.load() translates the JSON file back into a standard Python dictionary
    loaded_data = json.load(json_file)

print(f"Cluster {loaded_data['server_cluster']} has status {loaded_data['status']}")