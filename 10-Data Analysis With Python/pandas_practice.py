import pandas as pd

# Creating a Series representing storage limits for different cloud regions
limits_gb = pd.Series(
    [1000,500,250],
    index = ["us-east-1", "eu-west-1", "ap-south-1"]
)

print(limits_gb)
# Output:
# us-east-1     1000
# eu-west-1      500
# ap-south-1     250
# dtype: int64

# You can access data using the index label, just like a dictionary
print(limits_gb["eu-west-1"])  # Output: 500

# Sample audit data for artifact repositories
audit_data = {
    "repo_name": ["docker-prod", "npm-dev", "maven-release", "helm-charts", "pypi-local"],
    "size_gb": [150.5, 45.0, 500.2, 12.8, 85.5],
    "critical_vulns": [0, 12, 0, 2, 5],
    "owner_team": ["Platform", "Frontend", "Backend", "Platform", "Backend"],
    "is_compliant": [True, False, True, False, False]
}

df = pd.DataFrame(audit_data)
print(df)

# View the first 2 rows
print(df.head(2))

# Get a technical summary (data types, missing values, memory usage)
print(df.info())

# Get instant statistical metrics for numeric columns (count, mean, min, max, percentiles)
print(df.describe())

# Select a single column (returns a Series)
teams = df["owner_team"]

# Select multiple columns (returns a smaller DataFrame)
# Note the double brackets: the outer brackets are for selection, inner for a list of names
repo_summary = df[["repo_name", "size_gb"]]

# Grab the first row (index 0) using integer location
first_repo = df.iloc[0]

# Grab the first 3 rows, and only the "repo_name" and "critical_vulns" columns
subset = df.loc[0:2, ["repo_name", "critical_vulns"]]

# 1. Find all repositories larger than 100 GB
large_repos = df[df["size_gb"] > 100]

# 2. Find all non-compliant repositories owned by the Platform team
# Wrap each condition in parentheses () and use & (AND) or | (OR)
action_required = df[(df["is_compliant"] == False) & (df["owner_team"] == "Platform")]

print(action_required)

# 1. Group the dataframe by the 'owner_team' column
# 2. Select the 'size_gb' column
# 3. Apply the .sum() function

team_storage = df.groupby("owner_team")["size_gb"].sum()
print(team_storage)