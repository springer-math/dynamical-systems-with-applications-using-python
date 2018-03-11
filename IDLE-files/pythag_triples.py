# Part solution to Pythagorean triples.
# See Exercise 1(c).
# Run the Module (or type F5).

n = 1
m = 100
for a in range(1, m):
    for b in range(1, m):
        if a**2 + b**2 == (b+n) ** 2:
            print(a, b, b+n)
