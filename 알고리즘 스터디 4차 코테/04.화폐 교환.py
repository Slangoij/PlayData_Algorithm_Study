answer = 0
now_currency = []

def dfs(nowidx, left):
    if nowidx==len(now_currency)-1:
        if left%now_currency[nowidx]==0:
            global answer
            answer += 1
        return
        
    if nowidx>=len(now_currency) or left<0:
        return
    coin = now_currency[nowidx]
    for i in range(left//coin):
        dfs(nowidx+1, left-coin*i)

def solution(currencies, wantMoney):
    global now_currency, answer
    currencies.sort(reverse=True)

    for i in range(len(currencies)):
        if currencies[i] <= wantMoney:
            now_currency = currencies[i:]
            break

    dfs(0, wantMoney)
    
    return answer

currencies = [1,5,10]
wantMoney = 10
print(solution(currencies, wantMoney))






# # 1st try:
# def solution(currencies, wantMoney):
#     currencies.sort(reverse=True)

#     for i in range(len(currencies)):
#         if currencies[i] <= wantMoney:
#             now_current = currencies[i:]
#             break
        
#     answer = 0
#     leng = len(now_current)
#     for i in range(1<<leng):
#         now_money = wantMoney
#         for j in range(leng):
#             if i & (1<<j):
#                 now_money %= now_current[j]
#         if now_money == 0:
#             answer += 1

#     return answer