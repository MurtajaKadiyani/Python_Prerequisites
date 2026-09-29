def my_decorator(func):
    def wrapper():
        print("[BEFORE] Setting up execution environment...")
        func() # Executes the original function
        print("[AFTER] Cleaning up temporary files...")
    return wrapper  # Returns the inner function WITHOUT calling it

def deploy_app():
    print("-> Deploying application container to Kubernetes...")

# Manual decoration
deploy_app = my_decorator(deploy_app)

# Executing the decorated function
deploy_app()

@my_decorator
def deploy_app1():
    print("-> Deploying application container to Kubernetes...")

# Calling deploy_app now automatically triggers the wrapped version
deploy_app1()

import functools

def log_execution(func):
    # @functools.wraps preserves the original function's name and docstring
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[AUDIT LOG] Invoking: {func.__name__} with args={args}, kwargs={kwargs}")

        # Execute original function and store its result
        result = func(*args, **kwargs)

        print(f"[AUDIT LOG] {func.__name__} finished successfully.")
        return result
    return wrapper

@log_execution
def delete_repository(repo_name, force=False):
    """Deletes an artifact repository from inventory."""
    print(f"--> Purging repository '{repo_name}' (force={force})...")
    return {"status": "DELETED", "repo": repo_name}

# Calling the function
response = delete_repository("docker-local", force= True)
print("Return payload:", response)
