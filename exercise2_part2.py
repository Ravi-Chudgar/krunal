def decorator_to_str(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)  # Convert the result to a string
    return wrapper

@decorator_to_str
def add(a, b):
    return a + b

@decorator_to_str
def get_info(name, age):
    return f"Name: {name}, Age: {age}"

# Example usage:
result1 = add(10, 20)
result2 = get_info("Alice", 30)

print(result1)  # Output: "30"
print(result2)  # Output: "Name: Alice, Age: 30"
