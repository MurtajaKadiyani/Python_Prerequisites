from pathlib import Path

# Create a Path object. You can use forward slashes safely; 
# Python will automatically translate them to Windows backslashes if needed.
target_file = Path("E:/Applied AI Engineering/Python/6-File Handling/audit_report.json")

print("1. Full Path:", target_file)
print("2. Parent Directory:", target_file.parent)
print("3. Full File Name:", target_file.name)
print("4. File Extension:", target_file.suffix)
print("5. Name without Extension:", target_file.stem)

# Output:
# 1. Full Path: E:\Applied AI Engineering\Python\6-File Handling\audit_report.json (on Windows)
# 2. Parent Directory: E:\Applied AI Engineering\Python\6-File Handling
# 3. Full File Name: audit_report.json
# 4. File Extension: .json  
# 5. Name without Extension: audit_report

base_folder = Path("E:/Applied AI Engineering/Python/6-File Handling")
environment = "production"
filename = "settings.config"

# Use the / operator to join Path objects and strings seamlessly
final_path = base_folder / environment / filename
print(f"Consturcted Path:", final_path)

# Output on Windows: E:\Applied AI Engineering\Python\6-File Handling\production\settings.config

# Define a path to a folder that might not exist yet
backup_dir = Path("backup/server_01/september")

# Check if the folder exists
if not backup_dir.exists():
    print("Folder not found. Creating it now...")
    # mkdir() creates the folder.
    # parents=True means it will also create "backups" and "server_01" if they are missing.
    # exist_ok=True prevents crashes if the folder is created right before this line runs.
    backup_dir.mkdir(parents=True, exist_ok=True)

    print("Folder created succesfully!")
else:
    print("Folder alredy exists. Ready to write files.")


# Point to the directory containing your script
current_dir = Path(".")

# Create a few dummy text files for this example to find
(current_dir / "test1.txt").write_text("Hello")
(current_dir / "test2.txt").write_text("World")

print("Searching for .txt file:")

# .glob("*.txt") finds all text files in this exact folder.
# .rglob("*.txt") would search this folder AND all sub-folders (recursive).

for text_file in current_dir.glob("*.txt"):
    print(f"- Found: {text_file.name}")
    # Output:
    # Searching for .txt files:
    # - Found: test1.txt
    # - Found: test2.txt