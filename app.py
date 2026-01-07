# Simple calculator program with an intentional bug

def add_numbers(a, b):
    # BUG: wrong operation (- instead of +)
    return a - b

a = 10
b = 5

result = add_numbers(a, b)

# BUG: spelling mistake in output
print("Reslt =", result)
