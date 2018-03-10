# A function to convert degrees Fahrenheit to Kelvin.
# Save file as F2K.py.
# Run the Module (or type F5).
def F2K():
    F = int(input('Enter temperature in degrees Fahrenheit: '))
    K = (F + 459.67) * 5 / 9
    print('Temperature in Kelvin is {} K'.format(K))
