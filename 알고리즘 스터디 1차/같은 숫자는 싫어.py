def solution(arr):
    idx = 0
    lst = []
    lst.append(arr[0])
    while idx<len(arr)-1:
        if arr[idx]!=arr[idx+1]:
            lst.append(arr[idx+1])
        idx+=1
    return lst