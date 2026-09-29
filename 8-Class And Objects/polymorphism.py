# --- Define the Classes ---

class SlackNotifier:
    def trigger_alert(self,message):
      print(f"[SLACK API] posting to #devops-alerts: {message}")

class EmailNotifier:
   def trigger_alert(self,message):
      print(f"[SMTP SERVER] sending mail to on-call team: {message}")

class ServiceNowNotifier:
   def trigger_alert(self,message):
      print(f"[SERVICENOW] opening high-priority incident ticket:{message}")

# --- The Polymorphic Execution ---
# 1. We create objects from our different classes
slack = SlackNotifier()
email = EmailNotifier()
snow = ServiceNowNotifier()

notifications_channel = [slack,email,snow]

# 3. The Magic: A single loop handles everything
print("--- Initiating Incident Response ---")
for channel in notifications_channel:
   # Python automatically calls the correct version of trigger_alert() for each object
   channel.trigger_alert("CRITICAL: Authentication Service Offline")

class SecurityScanner:
   def scan(self):
      # A placeholder method meant to be overridden by child classes
      raise NotImplementedError("Subclass must implement abstract method")

class CodeScanner(SecurityScanner):
   def scan(self):
      return "Scanning Python source code for exposed password..."

class ContainerScanner(SecurityScanner):
   def scan(self):
      return "Scanning Docker image for outdated OS package..."
   

# You can now treat all scanners exactly the same way in your main script
scanners = [CodeScanner(), ContainerScanner()]

for scanner in scanners:
   result = scanner.scan()
   print(result)

print(len("Automation")) # String: Returns number of characters (10)
print(len(["Server1", "Server2"])) # List: Returns number of items (2)
print(len({"port": 80, "status": "up"}))  # Dictionary: Returns number of keys (2)
