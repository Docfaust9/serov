import numpy as np
import matplotlib.pyplot as plt
from itertools import *
import nashpy as nash

# Создаем матрицы выигрышей
A = np.array([[5, 3], [3, 8]])
B = np.array([[5, 15], [20, 5]])
'''A = np.array([[-10, 2], [1, -1]])
B = np.array([[5, -2], [-1, 1]])'''
print('A:')
[print(f'{item}') for item in A]
print('B:')
[print(f'{item}') for item in B]

# Ищем решения в чистых стратегиях
res_flag = False

for index, item in enumerate(A):
    max_column = A.T[index].argmax()
    max_row = B[index].argmax()
    if max_row == max_column:
        print(f'Решения в чистых стратегиях: A{max_column}{index} B{max_row}{index}')
        res_flag = True

if not res_flag:
    print('\nРешений в чистых стратегиях нет')

# Ищем решения в смешанных стратегиях
C = A[0][0] + A[1][1] - A[0][1] - A[1][0]
alpha = A[1][1] - A[0][1]
D = B[0][0] + B[1][1] - B[0][1] - B[1][0]
beta = B[1][1] - B[1][0]
uni_array = np.array([0, 0, 1, 1])
p_nesh = np.array([beta / D, 1 - beta / D])
q_nesh = np.array([alpha / C, 1 - alpha / C])
print(f'\nC= {C}\nalpha= {alpha}\nD= {D}\nbeta= {beta}')
print(f'\n[(p-1)*({C}q-{alpha})>=0\n[p*({C}q-{alpha})>=0')
print(f'\n[(q-1)*({D}p-{beta})>=0\n[q*({D}p-{alpha})>=0')
print(f'\n0<p<1 q=-{alpha}/{C}={alpha / C}')
print(f'0<q<1 p=-{beta}/{D}={beta / D}')
print('\np*=', p_nesh)
print('q*=', q_nesh)
buf_array = np.dot(p_nesh.T, A)
fa = np.dot(buf_array, q_nesh)
print('\nfA(p*,q*)=', fa)
buf_array = np.dot(p_nesh.T, B)
fb = np.dot(buf_array, q_nesh)
print('fB(p*,q*)=', fb)

# Ищем Парето оптимальное
array = []
best_point = [A[1][1], B[1][1]]
line_a = []
line_b = []
for i in range(len(A)):
    for j in range(len(A[0])):
        line_a.append(A[i][j])
        line_b.append(B[i][j])

print(line_a)

# Строим график вероятностей
nash, axes_nash = plt.subplots()
axes_nash.set_title('Равновесие по Нэшу')
p_a = np.array([0, beta / D, beta / D, 1])
q_b = np.array([1, alpha / C, alpha / C, 0])
axes_nash.set_xlabel('p')
axes_nash.set_ylabel('q')
axes_nash.plot(uni_array, p_a, label='p*')
axes_nash.plot(q_b, uni_array, label='q*')
axes_nash.legend()

# Строим график в множестве критериев
pareto, axes_pareto = plt.subplots()
axes_pareto.set_xlabel('A')
axes_pareto.set_ylabel('B')
axes_pareto.set_title('Оптимальность по Парето')
axes_pareto.fill(line_a, line_b)
x = [max(line_a), line_a[line_b.index(max(line_b))]]
y = [line_b[line_a.index(max(line_a))], max(line_b)]
axes_pareto.plot(x, y, c='red')
axes_pareto.scatter(fa, fb, c='orange')
for i in range(len(array)):
    for j in range(len(array[0])):
        axes_pareto.scatter(array[i][j][0], array[i][j][1], c='blue')

plt.show()
