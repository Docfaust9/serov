from prettytable import PrettyTable
import numpy as np
def init():
    Q = np.array([[5, 2, 8, 5], [4, 5, 9, 4], [4, 1, 7, 7], [4, 6, 9, 7], [1, 3, 4, 3], [0, 2, 3, 2], [1, 2, 4, 2],
                  [4, 3, 1, 0], [0, 0, 0, 0]])
    table_q = PrettyTable()
    table_q.field_names = ["x[i]", "z1", "z2", "z3", "z4"]
    for i in range(8):
        table_q.add_row([i+1,Q[i][0], Q[i][1], Q[i][2], Q[i][3]])
    beta=[]
    arr_trans=Q.transpose()
    beta = []
    for i in range(4):
        beta.append(arr_trans[i].max())
    table_q.add_row(["b",beta[0], beta[1], beta[2], beta[3]])
    print("Q:")
    print(table_q)
    print("R:")
    Q[8][0] = beta[0]
    Q[8][1] = beta[1]
    Q[8][2] = beta[2]
    Q[8][3] = beta[3]
    return Q

def R_matrix(Q):
    R=np.empty((8, 4))
    table_r = PrettyTable()
    table_r.field_names = ["x[i]", "z1", "z2", "z3", "z4"]
    for i in range(8):
        for j in range(4):
            R[i][j] = int(Q[8][j] - Q[i][j])
        table_r.add_row([i+1,R[i][0], R[i][1], R[i][2], R[i][3]])
    print(table_r)
    return R
def vald(Q):
    a=np.empty((8))
    table_vald = PrettyTable()
    table_vald.field_names = ["i", "a[i]"]
    for i in range(8):
        a[i]=(Q[i].min())
        table_vald.add_row([i+1, a[i]])
    print("1. Критерий Вальда: ")
    print(table_vald)
    max = a.max()
    number = []
    for i in range(8):
        if a[i]==max:
            number.append(i)
    for i in range(len(number)):
        print("Оптимальное решение по критерию Вальда: "+str(number[i]+1)+"e, значение x* = "+ str(a[number[i]]))
    return number

def maximum(Q):
    a=np.empty((8))
    table_max = PrettyTable()
    table_max.field_names = ["i", "a[i]"]
    for i in range(8):
        a[i]=(Q[i].max())
        table_max.add_row([i+1, a[i]])
    print("2. Критерий максимума: ")
    print(table_max)
    max = a.max()
    number = []
    for i in range(8):
        if a[i] == max:
            number.append(i)
    for i in range(len(number)):
        print("Оптимальное решение по критерию максимума: "+str(number[i]+1)+"e, значение x* = "+ str(a[number[i]]))
    return number

def savige(R):
    a=np.empty((8))
    table_sav = PrettyTable()
    table_sav.field_names = ["i", "a[i]"]
    for i in range(8):
        a[i]=(R[i].max())
        table_sav.add_row([i+1, a[i]])
    print("3. Критерий Сэвиджа: ")
    print(table_sav)
    sav = a.min()
    number = []
    for i in range(8):
        if a[i] == sav:
            number.append(i)
    for i in range(len(number)):
        print("Оптимальное решение по критерию Сэвиджа: "+str(number[i]+1)+"e, значение x* = "+ str(a[number[i]]))
    return number

def hurvic(Q, alpha):
    a=np.empty((8))
    table_hurv = PrettyTable()
    table_hurv.field_names = ["i", "a[i]"]
    for i in range(8):
        a[i]=round(alpha*(Q[i].min())+(1-alpha)*(Q[i].max())*10)/10
        table_hurv.add_row([i+1, a[i]])
    print("4. Критерий Гурвица: ")
    print(table_hurv)
    sav = a.max()
    number = []
    for i in range(8):
        if a[i] == sav:
            number.append(i)
    for i in range(len(number)):
        print("Оптимальное решение по критерию Гурвица: "+str((number[i])+1)+"e, значение x* = "+ str(a[number[i]]))
    return number

def laplas(Q):
    a = np.empty((8))
    table_sav = PrettyTable()
    table_sav.field_names = ["i", "a[i]"]
    for i in range(8):
        q_sum=0
        for j in range(4):
            q_sum+=Q[i][j]
        a[i] = 1/8 * q_sum
        table_sav.add_row([i + 1, a[i]])
    print("5. Критерий Лапласа: ")
    print(table_sav)
    sav = a.max()
    number = []
    for i in range(8):
        if a[i] == sav:
            number.append(i)
    for i in range(len(number)):
        print("Оптимальное решение по критерию Лапласа  : " + str(number[i] + 1) + "e, значение x* = " + str(a[number[i]]))
    return number

def bayes(Q, p):
    a = np.empty((8))
    table_sav = PrettyTable()
    table_sav.field_names = ["i", "a[i]"]
    for i in range(8):
        q_sum = -1
        for j in range(4):
            q_sum += p[j]*Q[i][j]
        a[i] = round(q_sum*10)/10
        table_sav.add_row([i + 1, a[i]])
    print("6. Критерий Байеса: ")
    print(table_sav)
    sav = a.max()
    number = []
    for i in range(8):
        if a[i] == sav:
            number.append(i)
    for i in range(len(number)):
        print("Оптимальное решение по критерию Байеса  : " + str(number[i] + 1) + "e, значение x* = " + str(a[number[i]]))
    return number

def matrix(vald_list,max_list, sav_list, hurv_list, laplas_list, bayes_list):
    all_lists =np.zeros((8, 6))
    for i in range(len(vald_list)):
        all_lists[vald_list[i]][0] += 1
    for i in range(len(max_list)):
        all_lists[max_list[i]][1] += 1
    for i in range(len(sav_list)):
        all_lists[sav_list[i]][2] += 1
    for i in range(len(hurv_list)):
        all_lists[hurv_list[i]][3] += 1
    for i in range(len(laplas_list)):
        all_lists[laplas_list[i]][4] += 1
    for i in range(len(bayes_list)):
        all_lists[bayes_list[i]][5] += 1
    print("Матрица выбора:")
    matrix_table = PrettyTable()
    matrix_table.field_names = ["проект", "Вальда", "Максимума", "Сэвиджа", "Гурвица", "Лапласа", "Байеса", "Сумма"]
    sum = []
    for i in range(8):
        sum.append(0)
        for j in range(6):
            sum[i]+=all_lists[i][j]
        matrix_table.add_row(["x"+str(i+1), all_lists[i][0], all_lists[i][1], all_lists[i][2], all_lists[i][3], all_lists[i][4],
                              all_lists[i][5], sum[i]])
    print(matrix_table)

def main():
    Q = init()
    R = R_matrix(Q)
    alpha = 0.6
    p = [0.1, 0.4, 0.4, 0.1]
    vald_list = []
    max_list = []
    sav_list = []
    hurv_list = []
    laplas_list = []
    bayes_list = []
    vald_list = vald(Q)
    max_list = maximum(Q)
    sav_list = savige(R)
    hurv_list = hurvic(Q, alpha)
    laplas_list = laplas(Q)
    bayes_list = bayes(Q, p)
    matrix(vald_list, max_list, sav_list, hurv_list, laplas_list, bayes_list)
if __name__=="__main__":
    main()