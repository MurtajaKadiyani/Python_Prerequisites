class StorageVolume:
    def __init__(self, name , size_gb):
        self.name = name
        self.size_gb = size_gb

    def __str__(self):
        return f"Volume '{self.name}': {self.size_gb}GB"

    # Overloading the '+' operator
    def __add__(self, other):
        # 1. Check if we are adding two StorageVolumes together
        if isinstance(other, StorageVolume):
            combined_name = f"{self.name} + {other.name}"
            combined_size = self.size_gb + other.size_gb

            # Return a brand new StorageVolume object
            return StorageVolume(combined_name, combined_size)
        # 2. Allow adding a raw integer (e.g., adding 50 GB directly)
        elif isinstance(other, int):
            return StorageVolume(self.name, self.size_gb + other)
        else:
            raise TypeError("Can only add another StorageVolume or an integer.")

# --- Testing the Overload ---
disk_A = StorageVolume("data-1", 500)
disk_B = StorageVolume("data-2", 250)

# 1. Adding two objects together
merged_disk = disk_A + disk_B
print(merged_disk)
# Output: Volume 'data-1 + data-2': 750GB

# 2. Adding an integer to an object
expanded_disk = disk_A + 100
print(expanded_disk) # Output: Volume 'data-1': 600GB

class ServerNode:
    def __init__(self, hostname, cpu_load):
        self.hostname = hostname
        self.cpu_load = cpu_load  # Percentage (0-100)

    def __repr__(self):
        return  f"{self.hostname}({self.cpu_load}%)"

    # Overload Less Than (<)
    def __lt__(self, other):
        if isinstance(other, ServerNode):
            return self.cpu_load < other.cpu_load
        return False

    # Overload Greater Than (>)
    def __gt__(self, other):
        if isinstance(other, ServerNode):
            return self.cpu_load > other.cpu_load
        return False


# --- Testing Comparisons and Sorting ---
node1 = ServerNode("Worker-01", 85)
node2 = ServerNode("Worker-02", 40)
node3 = ServerNode("Worker-03", 92)

# 1. Direct Comparison
print("Is node1 under less load than node2?", node1 < node2)  # Output: False
print("Is node1 under less load than node3?", node1 < node3)  # Output: True

# 2. Sorting entirely relies on __lt__
cluster = [node1, node2, node3]

print("\nUnsorted Cluster:", cluster)
# Output: [worker-01(85%), worker-02(40%), worker-03(92%)]

# Python uses your __lt__ method to figure out the order!
cluster.sort()

print("Sorted Cluster (Lowest load first):", cluster)
# Output: [worker-02(40%), worker-01(85%), worker-03(92%)]
