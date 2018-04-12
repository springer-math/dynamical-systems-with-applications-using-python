# Program 10a: Lienard Lyapunov quantities.
# Compute L(1) and L(2). Note, L(0)=-a_1.

from sympy import symbols,  solve

a2, a3, a4, a5 = symbols('a2 a3 a4 a5')
b2, b3, b4, b5 = symbols('b2 b3 b4 b5')
V30, V21, V12, V03 = symbols('V30 V21 V12 V03')

V3 = solve([3*V30 - 2*V12 - b2, V12, V21 + a2,
       2*V21 - 3*V03],
       [V30, V21, V12, V03])

print(V3)

V40, V31, V22, V13, V04, eta4 = symbols('V40 V31 V22 V13 V04 eta4')

V4 = solve([4*V40 - 2*V22 - b3+2 * a2**2,
            2*V22 - 4*V04,
            -eta4-V31-a3,
            V22,
            -2*eta4 + 3*V31 - 3*V13 + 2*a2*b2,
            -eta4 + V13],
            [V40, V31, V22, V13, V04, eta4])
print(V4)

# Set a3=2*a2*b2/3.
V50, V41, V32, V23, V14, V05 = symbols('V50 V41 V32 V23 V14 V05')

V5 = solve([5*V50 - 2*V32 - b4 + 10 * a2**2 * b2/3, 3*V32 - 4*V14,
            V14, -V41 - a4 +2*a2**3,
            4*V41 - 3*V23 + 2*a2*b3, 2*V23 - 5*V05],
            [V50, V41, V32, V23, V14, V05])
print(V5)

V60, V51, V42, V33, V24, V15, V06, eta6 = symbols('V60 V51 V42 V33 V24 V15 V06 eta6')

V6 = solve([6*V60 - 2*V42 - b5 + 6*a2*a4 + 4*a2**2 * b2**2 / 3 -8*a2**4,
            4*V42 - 4*V24 - 16*a2**4 / 3 - 4*a2**2 * b3/3 + 8*a2*a4 / 3,
            V24 - 6*V06,
            V42 + V24,
            -eta6 - V51 - a5 + 8*a2**3 * b2/3,
            -3*eta6 + 5*V51 - 3*V33 + 2*a2*b4 - 8*a2**3 * b2 - 2*a2*b2*b3 + 4*a4*b2,
            -3*eta6 + 3*V33 - 5*V15 - 16*a2**3 * b2/3 - 4*a2*b2*b3 / 3 + 8*a4*b2 / 3,
            -eta6 + V15],
            [V60, V51, V42, V33, V24, V15, V06, eta6])
print(V6)
