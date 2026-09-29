from abc import ABC , abstractmethod

# --- 1. The Abstract Base Class (The Blueprint) ---
class CloudStorage(ABC):

    @abstractmethod
    def authenticate(self):
        """Forces child classes to write authentication logic."""
        pass # We use 'pass' because the child class does the actual work

    @abstractmethod
    def upload(self, file_path):
        """Forces child classes to write upload logic."""
        pass

    # Abstract classes can also have normal, shared methods!
    def log_activity(self, action):
        print(f"[AUDIT LOG] Storage action performed: {action}")

# --- 2. The Child Classes (The Implementations) ---
class AzureStorage(CloudStorage):
    # We MUST implement both abstract methods, or Python will crash.
    def authenticate(self):
       print("Authenticate with Azure Managed Identity...")

    def upload(self, file_path):
       print(f"Uploading with {file_path} to Azure Blob Storage")
       self.log_activity("Upload to Azure")

class AWSStorage(CloudStorage):
    def authenticate(self):
         print("Authenticate with AWS IAM Roles...")

    def upload(self, file_path):
        print(f"Uploading with {file_path} to S3 Bucket")

# --- 3. Testing the Abstraction ---
# ERROR: You cannot instantiate an abstract class directly!
#storage = CloudStorage() # UNCOMMENTING THIS CAUSES A TypeError

# SUCCESS: Using the concrete child classes
print(("--- Azure Run ---"))
azure = AzureStorage()
azure.authenticate()
azure.upload("daily_backup.tar.gz")

print("\n--- AWS Run ---")
aws = AWSStorage()
aws.authenticate()
aws.upload("daily_backup.tar.gz")

class GoogleDriveStorage(CloudStorage):
    def authenticate(self):
        print("Logging into Google...")
    # FORGOT TO WRITE THE upload() METHOD!

# This crashes the moment you try to create the object:
# TypeError: Can't instantiate abstract class GoogleDriveStorage with abstract method upload
# GoogleDriveStorage()
