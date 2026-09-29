class APIClient:
    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint  # Public: Safe to access directly
        self.__api_key = api_key  # Private: Hidden from outside access

    def test_connection(self):
        # The class itself can access its own private variables internally
        print(f"Connecting to {self.endpoint} using key {self.__api_key[:4]}***")


# --- Testing the Object ---
client = APIClient("https://api.system.local", "xyz-987-secret")

# 1. Accessing a public variable works perfectly
print("Endpoint:", client.endpoint)
# 2. The internal method works perfectly
client.test_connection()
# 3. Attempting to access the private variable from the outside will CRASH
# print(client.__api_key) # UNCOMMENTING THIS CAUSES AN AttributeError!

class ServerConfig:
    def __init__(self, hostname, port):
        self.hostname = hostname
        # We assign to the property setter (not directly to a private variable)
        self.port = port

    # --- GETTER ---
    @property
    def port(self):
        """This runs when someone tries to READ the port."""
        return self.__port

    # --- SETTER ---
    @port.setter
    def port(self,value):
        """This runs when someone tries to CHANGE the port."""
        if not isinstance(value, int):
            print(f"[ERROR] Port must be a number. Invalid input: '{value}'")
            return

        if 1024 <= value <= 65535:
            self.__port  = value
            print(f"[SUCCESS] Port updated to {self.__port}")
        else:
            print(f"[ERROR] Port {value} is out of safe range (1024-65635).")

# --- Testing Validation ---
web_server = ServerConfig("web-01", 8080)

# Reading the value triggers the @property method
print(f"Current port: {web_server.port}")

# Attempting to set an invalid port (Blocked by the setter logic)
web_server.port = 80        # Fails (Out of range)
web_server.port = "eighty"  # Fails (Not an integer)

# Attempting a valid change
web_server.port = 4443      # Succeeds

print(f"New port: {web_server.port}")

