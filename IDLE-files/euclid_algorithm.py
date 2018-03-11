# Euclid's algorithm to find the gcd.
# See Exercise 10.
# Run the Module (or type F5).

a = 12348
b = 14238

while b != 0:
    d = a % b
    a = b
    b = d

print('The greatest common divisor is {}'.format(a))
