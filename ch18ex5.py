"""exercise 5: Write a version of this function with a single return statement that
uses two conditional expressions, one nested inside the other."""

def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n-1) + fibonacci(n-2)

# Test cases
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(2))  # 1
print(fibonacci(3))  # 2
print(fibonacci(4))  # 3
print(fibonacci(5))  # 5
print(fibonacci(6))  # 8
