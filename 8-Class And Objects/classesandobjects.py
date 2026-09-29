class Server:
    def __init__(self,hostname, ip_address, role):
        # Attributes (variables attached to this specific object)
        self.hostname = hostname
        self.ip_address = ip_address
        self.role = role
        self.is_running = False  # Default value for all new servers

    # Method (a function that belongs to this case)
    def start_server(self):
        """Powers on the server."""
        if not self.is_running:
            self.is_running = True
            print(f"[SUCCESS] {self.hostname} ({self.ip_address}) is now online.")
        else:
            print(f"[INFO] {self.hostname} is already running")

    def stop_server(self):
        """Powers off the server."""
        if self.is_running:
            self.is_running = False
            print(f"[SUCCESS] {self.hostname} has been SHUT DOWN.")
        else:
            print(f"[INFO] {self.hostname} is already powered off")

    def get_status(self):
        """Displays the current operational state."""
        state = "ONLINE" if self.is_running else "OFFLINE"
        return f"Server '{self.hostname} ({self.role}) is currently {state}'"


# Create two independent server objects from the same Server class
web_server = Server("web-prod-01", "10.0.0.15", "Web Frontend")
db_server = Server("db-prod-01", "10.0.0.22", "Database")

# 1. Accessing attributes using dot notation
print(f"Web Server Hostname: {web_server.hostname}")
print(f"Database IP address: {db_server.ip_address}")

# 2. Calling methods on specific objects
print("\n --- Initial States ---")
print(web_server.get_status())
print(db_server.get_status())

print("\n--- Performing Actions ---")
web_server.start_server() # Turns ON web_server
db_server.start_server()  # Turns ON db_server

print("\n--- Updated States ---")
print(web_server.get_status())

# Shutting down only one server
web_server.stop_server()

print(web_server.get_status())
print(db_server.get_status())  # db_server remains ONLINE independently!