def solution(x):
    answer = True
    nstr = str(x)
    leng = len(nstr)
    zari_sum = 0

    for i in range(0, leng):
        zari_sum += int(nstr[i])

    if x % zari_sum:
        answer = False
    return answer