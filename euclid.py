import math

# Euclidean Algorithm to find GCD
def euclidean_algorithm(a, b):
    return math.gcd(a, b)

# Example usage
number1 = 48
number2 = 18
gcd = euclidean_algorithm(number1, number2)
print(f"The GCD of {number1} and {number2} is: {gcd}")



# Extended Euclidean Algorithm
def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y

# Example usage
number1 = 48
number2 = 18
gcd, x, y = extended_euclidean_algorithm(number1, number2)
print(f"The GCD of {number1} and {number2} is: {gcd}")
print(f"Bézout coefficients (x, y) are: {x}, {y}")
