def solution(array, commands):
    answer = []
    lst = []
    i = j = k = 0
    for each_com in commands:
        # print(each_com)
        i = each_com[0]
        j = each_com[1]
        k = each_com[2]
        lst = array[i - 1:j]
        lst.sort()
        answer.append(lst[k - 1])
        lst.clear()

    return answer