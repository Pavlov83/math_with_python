from sympy import *
KnownVariable = 5
x = symbols('x')
y = symbols('y')
eq1 = Eq(5*x + 5*y - 7,0)
eq2 = Eq(0*x - 0*y - 9,0)
solution = solve((eq1),(x))
print(solution)