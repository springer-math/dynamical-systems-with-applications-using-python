# Sum of primes to N.
# Save file as sum_primes.py.
# Run the Module (or type F5).

n = int(input('What do you want to sum to? '))
sum_p = 0
for n in range(2, n+1):
    if all(n % i for i in range(2, n)):
        sum_p += n
print('The sum of the first {:,} primes is {:,}'.format(n, sum_p))
