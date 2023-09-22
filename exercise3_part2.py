def ignore_exception(exception_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type:
                return None
        return wrapper
    return decorator

# Example usage:
@ignore_exception(ZeroDivisionError)
def divide(a, b):
    return a / b

result1 = divide(10, 0)  # Returns None because it raises a ZeroDivisionError
result2 = divide(20, 5)  # Returns 4.0, no exception raised

print(result1)  # Output: None
print(result2)  # Output: 4.0
