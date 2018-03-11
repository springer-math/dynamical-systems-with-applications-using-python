# A program that sums the natural numbers to N.
# Save file as sum_n.py.
# Run the Module (or type F5).

def sum_n(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1  # increment counter

    print('The sum is', sum)
