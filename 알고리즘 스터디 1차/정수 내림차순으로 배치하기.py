def solution(n):
    answer = ''
    lst = []
    nstr = str(n)

    for i in range(0, len(nstr)):
        lst.append(int(nstr[i]))
    lst.sort(reverse=True)

    for i in lst:
        answer += str(i)
    answer = int(answer)

    return answer