# Sum of primes to N.
# Save file as sumP.py.
print('What do you want to sum to?')
N=input()
N=int(N)
sumP=0
for n in range(2,N+1):
    if all(n % i for i in range(2, n)):
        sumP += n
print('The sum of the first',n,'primes is',sumP)
    


