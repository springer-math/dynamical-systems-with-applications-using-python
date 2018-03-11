# A function to convert degrees Fahrenheit to degrees Centigrade.
# See Exercise 1(a).
# Save file as F2C.py.
# Run the Module (or type F5).
def F2C():
    F = int(input('Enter temperature in degrees Fahrenheit: '))
    C = (F - 32) * 5 / 9
    print('Temperature in degrees Centigrade is {} degrees C'.format(C))
