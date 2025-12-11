from decorators import round_result

@round_result(2)
def multiply(a, b):
    return a * b

print(multiply(3.14159, 2.71828))  # 8.54
