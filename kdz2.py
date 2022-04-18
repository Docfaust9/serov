from prettytable import PrettyTable
import random
import math
import pandas as pd
import matplotlib.pyplot as plt
def pareto_optim(x,y):#алгоритм исключения заведомо неэффективных решений
    global paret
    paret = []
    for i in range(len(x)):
        paret.append(i)
    for i in paret:
        for j in paret:
            if ((x[i] <= x[j]) and (y[i] < y[j])) or ((x[i] < x[j]) and (y[i] <= y[j])):
                paret.remove(j)
    return paret

def __checker(x1,y1,x,y): ## проверка на уникальность точки
    for i in range(len(x)):
        if x1 == x[i] and y1 == y[i]:
            return False
    return True

def find_angle():#поиск угловых коэффицентов ограничений конуса доминирования
    nu1min = 0.2
    nu1max = 0.5
    nu2min = 0.3
    nu2max = 0.8
    points_x = []
    points_y = []
    x = 0
    while(len(points_x) < 2):
        y = - x + 1
        if (y == nu2min) and (x >= nu1min) and (x <= nu1max):
            points_x.append(x)
            points_y.append(y)
        elif (y == nu2max) and (x >= nu1min) and (x <= nu1max):
            points_x.append(x)
            points_y.append(y)
        elif (x == nu1min) and (y >= nu2min) and (y <= nu2max):
            points_x.append(x)
            points_y.append(y)
        elif (x == nu1max) and (y >= nu2min) and (y <= nu2max):
            points_x.append(x)
            points_y.append(y)
        x =round(x + 0.1, 1)
        if x > 1:
            break
    #cos_angle = (points_x[0]*points_x[1] + points_y[0]*points_y[1])/(math.sqrt(points_x[0]**2+points_y[0]**2))*(math.sqrt(points_x[1]**2+points_y[1]**2))
    #return cos_angle
        global tg_a
        global tg_b
    tg_a = -1/(points_y[0]/points_x[0])
    tg_b = -1/(points_y[1]/points_x[1])

def generate_points():
    global j1,j2
    j1 = []
    j2 = []
    while(len(j1)<100):
        u1 = random.randint(0,79)
        u2 = random.randint(0,79)
        buf = ((0.2 * (u1 - 70) * (u1 - 70)) + (0.8 * (u2 - 20) * (u2 - 20)))
        buf1 = ((0.2 * (u1 - 10) * (u1 - 10)) + (0.8 * (u2 - 70) * (u2 - 70)))

        if __checker(buf,buf1, j1,j2):
            print(buf)
            j1.append(buf)
            print(buf1)
            j2.append(buf1)
    print(j1[1],j2[1])

def __angle_point(x,y, x1, y1):
    if (x-x1 == 0):
        return 1000
    else:
        return (y-y1)/(x-x1)

def omega_opt(j1,j2):
    global omega
    omega=[]
    for i in range(len(j1)):
        omega.append(i)
    for i in omega:
        for j in omega:
            if (i != j):
                if ((__angle_point(j1[i],j2[i],j1[j],j2[j]) > tg_a) and (j1[i]-j1[j]<0))or ((__angle_point(j1[i],j2[i],j1[j],j2[j]) < tg_b) and (j1[i]-j1[j]>0)) or (j1[i]<j1[j] and j2[i]<j2[j]):
                    omega.remove(j)

    return omega
generate_points()
find_angle()
pareto_optim(j1,j2)
omega_opt(j1,j2)

print("Парето-оптимальные точки: ", *paret)
print("Омега оптимальные точки:", *omega)
omega_x = []
omega_y = []
omega_list = omega
for i in omega_list:
    omega_x.append(j1[i])
    omega_y.append(j2[i])
pareto_x = []
pareto_y = []
pareto_list = paret
for i in pareto_list:
    pareto_x.append(j1[i])
    pareto_y.append(j2[i])
df = pd.DataFrame({'j1': j1,'j2': j2})
plt.scatter(df['j1'], df['j2'])
df = pd.DataFrame({'f1': pareto_x,'f2': pareto_y})
plt.scatter(df['f1'], df['f2'],c='green')
df = pd.DataFrame({'c1': omega_x,'c2': omega_y})
plt.scatter(df['c1'], df['c2'],c='black')

plt.show()


