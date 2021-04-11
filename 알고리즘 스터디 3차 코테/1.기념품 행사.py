def solution(goods):
    answer = 0
    goods.sort()
    
    for go in goods:
        if go >= 50:
            answer += go - 10
            goods.remove(go)

    if len(goods)>1:
        now_price = goods[-1]
        if now_price + goods[0] >= 50:
            answer += now_price + goods[0] - 10
            goods.remove(now_price)
            goods.remove(goods[0])
    
    if len(goods)>1:
        now_price = goods[-1]
        if now_price + goods[0] >= 50:
            answer += goods[0] + goods[-1] - 10
            goods.pop(goods[-1])
            goods.pop(goods[0])

    if sum(goods) >= 50:
        answer += sum(goods) - 10
    else:
        answer += sum(goods)

    return answer

print(solution([1,23,24]))
# print(solution([1,23,49]))
# print(solution([99,99,99]))



# # 1st try: 한가지 테스트케이스 실패
# def solution(goods):
#     answer = 0
#     goods.sort()    

#     now_price = 0
#     for idx in [0,2,1]:
#         now_price += go
#         if now_price >= 50:
#             answer += now_price-10
#             now_price = 0

#     if now_price:
#         return now_price

#     return answer
