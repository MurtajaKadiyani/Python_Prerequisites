import pandas as pd
import numpy as np

# Sample raw audit dataset with missing and messy values
raw_data = {
    "repo_name": [" Docker-Prod ", "npm-dev", "MAVEN-release", "helm-charts", None],
    "size_mb": [150500, 45000, np.nan, 12800, 85500],
    "vuln_count": [0, 12, 0, np.nan, 5]
}

df = pd.DataFrame(raw_data)
# 1. Clean string column: handle missing names, trim spaces, convert to lowercase
df["repo_name"] = df["repo_name"].fillna("unknown-repo").str.strip().str.lower()

# 2. Fill missing numeric values: replace NaN with median size
median_size = df["size_mb"].median()
df["size_mb"] = df["size_mb"].fillna(median_size)

# 3. Fill missing integers and enforce integer data type
df["vuln_count"] = df["vuln_count"].fillna(0).astype(int)

print(df)

# Convert MB to GB and flag repositories larger than 50 GB
df["size_gb"] = df["size_mb"] / 1024

df["is_large"] = np.where(df["size_gb"] > 50, True, False)

# Assign a security risk level based on vulnerability thresholds
conditions  = [
    (df["vuln_count"] >= 10),
    (df["vuln_count"] > 0) & (df["vuln_count"] < 10),
    (df["vuln_count"] == 0)
]

choices = ["HIGH_RISK", "MEDIUM_RISK", "LOW_RISK"]

df["risk_tier"] = np.select(conditions, choices, default="UNKNOWN")
print(df[["repo_name", "vuln_count", "risk_tier"]])

# Ownership lookup table
teams_data = {
    "repo_name": ["docker-prod", "npm-dev", "maven-release", "helm-charts"],
    "owner_team": ["Platform", "Frontend", "Backend", "Platform"]
}

teams_df = pd.DataFrame(teams_data)

# Perform a LEFT JOIN on 'repo_name'
merged_df = pd.merge(df, teams_df, on="repo_name", how="left")

# Fill unmapped repositories with 'Unassigned'
merged_df["owner_team"] = merged_df["owner_team"].fillna("Unassigned")

print(merged_df[["repo_name", "owner_team", "size_gb", "risk_tier"]])

team_metrics = merged_df.groupby("owner_team").agg(
    total_repos=("repo_name", "count"),
    total_gb=("size_gb", "sum"),
    max_vulns=("vuln_count", "max")
).reset_index()

print(team_metrics)

# Cross-tabulate storage size across Teams (rows) and Risk Tiers (columns)
pivot_report = pd.pivot_table(
    merged_df,
    values="size_gb",
    index="owner_team",
    columns="risk_tier",
    aggfunc="sum",
    fill_value=0  # Replace NaN results with 0
)

print(pivot_report)

import pandas as pd
import numpy as np

def process_audit_pipeline(raw_repos_df, team_lookup_df):
    # Step 1: Clean and standardize strings
    df = raw_repos_df.copy()
    df["repo_name"] = df["repo_name"].fillna("unknown").str.strip().str.lower()
    
    # Step 2: Handle missing numerical data
    df["size_mb"] = df["size_mb"].fillna(df["size_mb"].median())
    df["vuln_count"] = df["vuln_count"].fillna(0).astype(int)
    
    # Step 3: Vectorized transformations (MB -> GB and Risk Classification)
    df["size_gb"] = df["size_mb"] / 1024
    
    risk_conditions = [
        (df["vuln_count"] >= 10),
        (df["vuln_count"] > 0),
        (df["vuln_count"] == 0)
    ]
    risk_labels = ["CRITICAL", "WARNING", "HEALTHY"]
    df["status"] = np.select(risk_conditions, risk_labels, default="UNKNOWN")
    
    # Step 4: Merge metadata
    final_df = pd.merge(df, team_lookup_df, on="repo_name", how="left")
    final_df["owner_team"] = final_df["owner_team"].fillna("Unassigned")
    
    # Step 5: Summary pivot table
    summary_pivot = pd.pivot_table(
        final_df,
        values="size_gb",
        index="owner_team",
        columns="status",
        aggfunc="sum",
        fill_value=0.0
    )
    
    return final_df, summary_pivot

# --- Test Pipeline Execution ---
raw_df = pd.DataFrame({
    "repo_name": [" Docker-Prod ", "npm-dev", "MAVEN-release", "helm-charts", None],
    "size_mb": [150500, 45000, np.nan, 12800, 85500],
    "vuln_count": [0, 12, 0, np.nan, 5]
})

teams_df = pd.DataFrame({
    "repo_name": ["docker-prod", "npm-dev", "maven-release", "helm-charts"],
    "owner_team": ["Platform", "Frontend", "Backend", "Platform"]
})

cleaned_data, audit_summary = process_audit_pipeline(raw_df, teams_df)

print("--- Cleaned & Transformed Dataset ---")
print(cleaned_data[["repo_name", "owner_team", "size_gb", "status"]])

print("\n--- Storage (GB) by Team & Status ---")
print(audit_summary)