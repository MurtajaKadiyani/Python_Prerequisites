# --- Parent Class (Base) ---
class User:
    def __init__(self, username, email): 
        self.username = username
        self.email = email
        self.is_active = True

    def get_info(self):
        """Displays standard profile info."""
        status = "Active" if self.is_active else "Inactive"
        return f"User: {self.username} <{self.email}> [{status}]"

    def deactivate(self):
        """Deactivates the account."""
        self.is_active = False
        print(f"[ACCOUNT] {self.username}'s account has been deactivated.")

# --- Child Class 1: DeveloperUser ---
class DeveloperUser(User):
    def __init__(self, username, email, primary_language):
        # super() calls the __init__ of the parent User class
        super().__init__(username, email)
        self.primary_language = primary_language  # Extra attribute unique to Developers

    def write_code(self):
        """Developer-specific method."""
        print(f"[DEV] {self.username} is writing code in {self.primary_language}.")

# --- Child Class 2: AdminUser ---
class AdminUser(User):
    def __init__(self, username, email, security_clearance):
        super().__init__(username, email)
        self.security_clearance = security_clearance

     # 1. Method Overriding: Changing how get_info works specifically for Admins
    def get_info(self):
    # We can call super().get_info() to get the base string, then append extra data
      base_info = super().get_info()
      return f"{base_info} | Clearance Level: {self.security_clearance}"
    # 2. Admin-specific method
    def revoke_access(self, target_user):
      print(f"[SECURITY] Admin {self.username} is revoking access for {target_user.username}...")
      target_user.deactivate()

# Create an instance of DeveloperUser
dev = DeveloperUser("alex_dev","alex@company.com","Python")

# Create an instance of AdminUser
admin = AdminUser("Murtaja_admin","murtaja@company.com","Level-3")

# 1. Developer using both inherited methods AND unique methods
print(dev.get_info())  # Inherited from User
dev.write_code()       # DeveloperUser method

print("\n" + "="*40 + "\n")

# 2. Admin using overridden method
print(admin.get_info())  # Customized in AdminUser
print("\n" + "="*40 + "\n")

# 3. Admin performing an action on the Developer account
admin.revoke_access(dev)

# 4. Verify dev account is now deactivated
print(dev.get_info())

# Check if an object belongs to a class or parent class
print(isinstance(dev,DeveloperUser)) # True
print(isinstance(dev,User)) # True (since DeveloperUser inherits from User)

# Check class relationship
print(issubclass(AdminUser,User))  # True
