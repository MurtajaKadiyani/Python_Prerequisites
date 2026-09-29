servers = ["web-01", "db-01"]

# 1. Python calls iter() on the iterable to get an Iterator engine
server_iterator = iter(servers)  # Under the hood: servers.__iter__()

# 2. Python calls next() to get each item
print(next(server_iterator))  # Output: web-01
print(next(server_iterator))  # Output: db-01

# 3. When it runs out, next() raises StopIteration, which the 'for' loop catches silently.
# print(next(server_iterator)) -> raises StopIteration!

class RepositoryPaginator:
    """An iterator that generates repository names sequentially."""

    def __init__(self, prefix, total_count):
        self.prefix = prefix
        self.total_count = total_count
        self.current_index = 1  # State: keeps track of where we are

    def __iter__(self):
        # A true iterator must return itself in __iter__
        return self

    def __next__(self):
        # 1. Check if we have reached the limit
        if self.current_index > self.total_count:
          # 2. Signal that the loop should end
          raise StopIteration

        # 3. Generate the data
        repo_name = f"{self.prefix}-repo-{self.current_index}"

        # 4. Advance the state for the next call
        self.current_index += 1

        return repo_name

# --- Using the Custom Iterator ---

# Initialize the iterator
docker_repos = RepositoryPaginator(prefix="docker-local", total_count=3)

# The for loop automatically handles __iter__(), __next__(), and StopIteration
for repo in docker_repos:
    print(f"Scanning: {repo}")