from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    dq = deque([0]*bridge_length)
    for i in truck_weights:
        if weight < i:
            for _ in range(bridge_length-1):
                if dq[0] == i:
                    break
                weight += dq.popleft()
                dq.append(0)
                answer += 1
        dq.append(i)
        weight += dq.popleft()
        weight -= i
        answer += 1

    answer += len(dq)

    return answer


# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

# bridge_length = 4
# weight = 2
# truck_weights = [1]*4

bridge_length = 4
weight = 10
truck_weights = [1,10,1,10]

print(solution(bridge_length, weight, truck_weights))
