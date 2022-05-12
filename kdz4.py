import numpy as np
from scipy import optimize

d1 = 2
d2 = 1
f1 = [-1,-1]
lhs_ineq = [[1,2],[-2,-1],[-1,0],[1,0],[0,-1],[0,1]]
rhs_ineq = [28,-7,0,14,0,10.5]
res1 = optimize.linprog(c=f1, A_ub=lhs_ineq, b_ub=rhs_ineq,method='revised simplex')
print('Координаты точки x1*({} ; {})'.format(res1.x[0],res1.x[1]), 'f1*:', round(res1.fun*-1, ndigits=2))
print("Назначу уступку d1 = {} на f1".format(d1))

f2 = [3,-1]
lhs_ineq = [[1,2],[-2,-1],[-1,0],[1,0],[0,-1],[0,1],[-1,-1]]
rhs_ineq = [28,-7,0,14,0,10.5,-19]
res2 = optimize.linprog(c=f2, A_ub=lhs_ineq, b_ub=rhs_ineq,method='revised simplex')
print('Координаты точки x2*({} ; {})'.format(res2.x[0],res2.x[1]), 'f2*:', round(res2.fun*-1, ndigits=2))
print("Назначу уступку d2 = {} на f2".format(d2))

f3 = [-1,3]
lhs_ineq = [[1,2],[-2,-1],[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[3,-1]]
rhs_ineq = [28,-7,0,14,0,10.5,-25,22]
res3 = optimize.linprog(c=f3, A_ub=lhs_ineq, b_ub=rhs_ineq,method='revised simplex')
print("Оптимальное решение: [{} ; {}], f1 = {}, f2 = {}, f3 = {}".format(res3.x[0],
res3.x[1],
round(res1.fun*-1, ndigits=2)-2,
round(res2.fun*-1, ndigits=2)-1,
round(res3.fun*-1, ndigits=2)))
