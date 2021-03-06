def solution(dirs):
    answer = 0

    hor_map = ver_map = [[False] * 10 for _ in range(10)]
    now_pos = [5,5]

    for move in dirs:
        if move == 'U':
            if now_pos[0]:
                if not ver_map[now_pos[0]-1][now_pos[1]]:
                    ver_map[now_pos[0]-1][now_pos[1]] = True
                    answer += 1
                now_pos[0] -= 1
        elif move == 'D':
            if now_pos[0] < 10:
                if not ver_map[now_pos[0]+1][now_pos[1]]:
                    ver_map[now_pos[0]+1][now_pos[1]] = True
                    answer += 1
                now_pos[0] += 1
        elif move == 'L':
            if now_pos[1]:
                if not hor_map[now_pos[0]][now_pos[1]-1]:
                    hor_map[now_pos[0]][now_pos[1]-1] = True
                    answer += 1
                now_pos[1] -= 1
        else:
            if now_pos[1] < 10:
                if not hor_map[now_pos[0]][now_pos[1]+1]:
                    hor_map[now_pos[0]][now_pos[1]+1] = True
                    answer += 1
                now_pos[1] += 1

    return answer

dirs = "ULURRDLLU"

print(solution(dirs))