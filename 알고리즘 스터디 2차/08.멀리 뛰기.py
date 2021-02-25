# 3rd try:
def solution(n):
    cache = [0] * (n+2)
    cache[1] = 1

    for i in range(2, n+2):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[n+1]



# # 2nd try:
# def solution(n):
#     ans = 0
#     if n <= 1:
#         return 1
#     else:
#         return solution(n-1) + solution(n-2)
#
# for i in range(1, 101):
#     print(solution(i))

# # 1st try:
# def cal_com(ttl, num):
#     if num == ttl or num == 0:
#         return 1
#     else:
#         up = down = 1
#         for _ in range(num):
#             up *= ttl
#             down *= num
#             ttl -= 1
#             num -= 1
#         return int(up / down)
#
#
# def solution(n):
#     answer = 0
#     total = nownum = n
#
#     while total >= 0 and nownum >= 0:
#         answer += cal_com(total, nownum)
#         total -= 1
#         nownum -= 2
#
#     return answer
#
#
# for i in range(1, 101):
#     print(solution(i))
#
# # print(solution(4))
# # print(cal_com(3,2))
