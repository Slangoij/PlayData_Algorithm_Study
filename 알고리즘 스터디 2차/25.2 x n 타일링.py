# 2nd try:
def solution(n):
    answer = 0
    
    if n > 2:
        a = 1
        b = 2
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return c%1000000007
    elif n == 2:
        return 2
    else:
        return 1
    
        

print(solution(4))




# # 1st try: 리스트를 활용하여 시간초과가 났다고 한다
# def solution(n):
#     answer = 0
    
#     if n>1:
#         lst = [0 for _ in range(n)]
#         for i in range(2):
#             lst[i] = 1
#         for i in range(2, n):
#             lst[i] = lst[i-1] + lst[i-2]
#         return lst[-1]%1000000007
#     else:
#         return 1