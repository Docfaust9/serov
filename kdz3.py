from scipy import optimize
obj = [-1,-1]
lhs_ineq = [[-1,-1],[1,-2],[-3,2],[3,-1],[-1,3],[-1,0],[1,0],[0,-1],[0,1]]
rhs_ineq = [-14,7,14,14,42,0,28,0,21]
res = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,method='revised simplex')
print('Оптимальное значение:', round(res.fun*-1, ndigits=2),
      '\nКоординаты точки:', res.x,
      '\nКоличество выполненных итераций:', res.nit,
      '\nСтатус:', res.message)
print('Значение функции f2 в оптимальной точке:',(-3*res.x[0] + res.x[1]))
print('Значение функции f3 в оптимальной точке:',(res.x[0] + (-3)*res.x[1]))