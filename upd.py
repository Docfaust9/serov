from prettytable import PrettyTable
import random

def find_b(x1,y1,x,y):
    count=0
    for i in range(len(x)):
        if ((x[i]>=x1) and (y[i]>y1)) or ((x[i]>x1) and (y[i]>=y1)):
            count+=1
    return count

def find_f(b,number):
    return (1/(1+b/(number-1)))

def find_k(f):
    k1 = abs(1-f)
    k2 = abs(0.85-f)
    k3 = abs(0.75-f)
    if (k1>k2) and (k2>k3):
        return 3
    elif (k1>k2) and (k3>=k2):
        return 2
    else:
        return 1

def __checker(x1,y1,x,y): ## проверка на уникальность точки
    for i in range(len(x)):
        if x1 == x[i] and y1 == y[i]:
            return False
    return True

def rand_points(x,y):
    n = 7
    while (len(x) != 600):
        x1 = random.randint(0, 20 * n)/10
        y1 = random.randint(0, 20 * n)/10
        if ((x1 - n) ** 2 + (y1 - n) ** 2 <= n ** 2) and (-x1 + y1 <= n) and (x1 + y1 >= 2 * n) and __checker(x1,y1,x,y):
            x.append(x1)
            y.append(y1)
def main():
    table = PrettyTable()
    table.add_column("i", ["f1", "f2", "bi", "Фi", "K"]) ## задаем параметры таблицы
    x = []
    y = []
    b = [] ## bi
    f = [] ## Фi
    k = [] ##Ki
    rand_points(x,y)
    number = len(x)
    for i in range(number):
        b.append(find_b(x[i],y[i],x,y))
        f.append(round(find_f(b[i],number), 3))
        k.append(find_k(f[i]))
        table.add_column (str(i+1),[x[i], y[i], b[i], f[i], k[i]]) ## заносим данные в таблицу
    print(table) ##вывод таблицы
if __name__ == "__main__":
    main()