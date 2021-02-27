def solution(arr1, arr2):
    answer = [[]]
    answer.clear()
    for i in range(0,len(arr1)):
        tmp = []
        for j in range(0,len(arr1[i])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)
    return answer