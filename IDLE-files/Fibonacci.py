# A function to list the n terms of the Fibonacci sequence.
# Save file as Fibonacci.py.
# Run the Module (or type F5). 
def Fibonacci(n):
    a,b = 0,1
    print(a),print(b),print(a+b)
    for i in range(n-3):
        a,b = b,a+b
        print(a+b)
