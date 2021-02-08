def solution(s):
    answer = ''
    s = s.split()
    ints = []
    for i in s:
        ints.append(int(i))

    xnum = max(ints)
    nnum = min(ints)

    answer = str(nnum) + ' ' + str(xnum)
    return answer

print(solution("-1 -2 -3 -4"))