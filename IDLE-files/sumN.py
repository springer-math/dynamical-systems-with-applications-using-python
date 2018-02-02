# A program that sums the natural numbers to N.
# Save file as sumN.py.
def sumN(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i = i+1    # update counter

    print('The sum is', sum)
