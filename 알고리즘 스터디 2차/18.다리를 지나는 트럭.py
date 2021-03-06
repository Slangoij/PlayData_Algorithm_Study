from collections import deque

# 2nd try:
def solution(bridge_length, weight, truck_weights):
    answer = 0
    dq = deque([0]*bridge_length)
    for i in truck_weights:
        while dq[0] + weight < i:
            dq.append(0)
            weight += dq.popleft()
            answer += 1
        dq.append(i)
        weight -= i
        weight += dq.popleft()
        answer += 1

    answer += len(dq)

    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))



# bridge_length = 4
# weight = 10
# truck_weights = [10,10,10,10]

# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

# bridge_length = 4
# weight = 2
# truck_weights = [1]*4




# # 1st try:
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#
#     dq = deque([0]*bridge_length)
#
#     dq = [0007] 7
#     [0007]  4
#     10
#     for i in truck_weights:
#         if weight < i:
#             for _ in range(bridge_length-1):
#                 if dq[0] <= i:
#                     break
#                 weight += dq.popleft()
#                 dq.append(0)
#                 answer += 1
#         dq.append(i)
#         weight += dq.popleft()
#         weight -= i
#         answer += 1
#
#     answer += len(dq)

    return answer