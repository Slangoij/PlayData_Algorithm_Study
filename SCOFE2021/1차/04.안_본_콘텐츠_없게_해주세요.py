num = list(map(float, input().split()))

tmplst = list(map(int, input().split()))
N, M = tmplst[0], tmplst[1]

yeol = []
conten = []
for _ in range(N):
    yeol.append(list(input()))
for _ in range(N):
    conten.append(list(input()))

def con_to_num(con):
    if con == 'A':
        return num[0]
    if con == 'B':
        return num[1]
    if con == 'C':
        return num[2]
    if con == 'D':
        return num[3]
    if con == 'E':
        return num[4]

lst = []
for i in range(N):
    for j in range(M):
        if yeol[i][j] != 'W':
            if yeol[i][j] == 'Y':
                tmp_num = 0
            else:
                tmp_num = 1
            lst.append((tmp_num, conten[i][j], con_to_num(conten[i][j]), i, j))

lst.sort(key=lambda x: (x[0], -x[2]))

for i in lst:
    print(f'{i[1]} {i[2]} {i[-2]} {i[-1]}')