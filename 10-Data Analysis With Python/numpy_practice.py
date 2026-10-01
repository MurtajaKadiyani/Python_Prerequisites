import numpy as np

# A standard 1D array representing artifact sizes in Megabytes
artifact_sizes_mb = np.array([150.5, 45.2, 1024.0, 500.75, 8.5])

print(type(artifact_sizes_mb))  # Output: <class 'numpy.ndarray'>
print(artifact_sizes_mb)  # Output: [150.5   45.2 1024.   500.75   8.5 ]

# Create an array of 5 zeros
zero_metrics = np.zeros(5) # [0. 0. 0. 0. 0.]

# Create an array of sequential numbers from 0 to 10 (exclusive), stepping by 2
sequence = np.arange(0, 10, 2)  # [0 2 4 6 8]

# Convert all sizes from MB to GB
# In standard Python, you would need a list comprehension: [x / 1024 for x in artifact_sizes_mb]

# In NumPy, you just divide the array directly:
artifact_sizes_gb = artifact_sizes_mb / 1024

print("Sizes in GB:", artifact_sizes_gb)
# Sizes in GB: [0.14697266 0.04414062 1.         0.48901367 0.00830078]

downloads = np.array([100, 500, 2, 50, 1000])
total_bandwidth_mb = artifact_sizes_mb * downloads

print("Bandwidth (MB):", total_bandwidth_mb) # Bandwidth (MB): [15050.   22600.    2048.   25037.5   8500. ]

data_matrix = np.array([
    [10, 20, 30],
    [40, 50 ,60]
])
print(data_matrix.shape)  # Output: (2, 3) -> 2 rows, 3 columns
print(data_matrix.ndim)   # 2 -> Number of dimensions (2D array)
print(data_matrix.size)   # 6 -> Total number of elements in the array
print(data_matrix.dtype)  # int64 -> The data type of the elements

# 1. Create a boolean mask (returns an array of True/False)
is_large = artifact_sizes_mb > 400
print(is_large)  # Output: [ True False  True  True False]

# 2. Apply the mask to the original array to filter it
large_artifacts = artifact_sizes_mb[is_large]
print("Large artifacts (MB):", large_artifacts)  # Output: [150.5 1024.  500.75]

# Shorthand notation (combining both steps)
large_artifacts = artifact_sizes_mb[artifact_sizes_mb > 400]

print("Artifacts > 400MBu6:", large_artifacts)  # Artifacts > 400MB: [1024.    500.75]

# Using our artifact array: [ 150.5    45.2  1024.     500.75    8.5 ]
total_storage = np.sum(artifact_sizes_mb)  # Sum of all artifact sizes
average_size = np.mean(artifact_sizes_mb)  # Average size of artifacts
largest_file = np.max(artifact_sizes_mb)  # Largest artifact size
smallest_file = np.min(artifact_sizes_mb)  # Smallest artifact size

print(f"Total Storage: {total_storage} MB") # 1728.95 MB
print(f"Average Size:  {average_size} MB")  # 345.79 MB
print(f"Largest:       {largest_file} MB")  # 1024.0 MB
print(f"Smallest:      {smallest_file} MB")  # 8.5 MB
