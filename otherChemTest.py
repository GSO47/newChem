from sympy import Matrix
from pprint import pprint

p = Matrix([[-1/4,1/4], [9/8,-5/8]])
p_inv = p.inv()
A = Matrix([[0,2],[1,-1]])

pprint(p_inv * A * p)
v = Matrix([2,-5])