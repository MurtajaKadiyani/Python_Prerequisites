class Artifacts:
    def __init__(self, name, version, size_mb):
        self.name = name
        self.version = version
        self.size_mb = size_mb

    # 1. Developer / Debugging View
    def __repr__(self):
        # Ideally looks like valid Python code to recreate the object
        return f"Artifact(name='{self.name}', version='{self.version}',size_mb={self.size_mb})"
    
    # 2. User Friendly View
    def __str__(self):
        return f"{self.name}:{self.version}({self.size_mb} MB)"

    # 3. Equality Comparison (==)
    def __eq__(self, other):
        # First ensure 'other' is also an Artifact object
        if isinstance(other, Artifacts):
            # Two artifacts are equal if name and version match
            return self.name == other.name and self.version == other.version
        return False

# --- Demonstration ---
art1 = Artifacts("app-service", "v1.2.0", 250)
art2 = Artifacts("app-service", "v1.2.0", 250)
art3 = Artifacts("app-service", "v2.0.0", 310)

# --- 1. Testing __str__ and __repr__ ---
print("--- Printing Objects (__str__) ---")
print(art1)  # Output: app-service:v1.2.0 (250 MB)
print(f"Deploying {art3}") # Output: Deploying app-service:v2.0.0 (310 MB)


print("\n--- Objects Inside a List (__repr__) ---")
inventory = [art1, art3]
print(inventory)  
# Output: [Artifact(name='app-service', version='v1.2.0', size_mb=250), Artifact(name='app-service', version='v2.0.0', size_mb=310)]

# --- 2. Testing Equality (__eq__) ---
print("\n---Testing Equality ---")
print("art1 == art2:", art1 == art2)  # Output: True (same name & version)
print("art1 == art3:", art1 == art3)  # Output: False (different versions)

class Repository:
    def __init__(self, name, artifacts): 
        self.name = name
        self.artifacts = artifacts  # List of Artifact objects

    # Allows len(repo_object)
    def __len__(self):
        return len(self.artifacts)

    # Allows item access like repo[0]
    def __getitem__(self, index):
        return self.artifacts[index]

    # Allows truthiness testing: bool(repo)
    def __bool__(self):
        return len(self.artifacts) > 0

# --- Usage ---
repo = Repository("docker-local", [art1,art3])

print("Repo artifact count:", len(repo)) # Output: 2
print("First item in repo:", repo[0])  # Output: app-service:v1.2.0 (250 MB)

if repo:
    print("Repository is not empty!")