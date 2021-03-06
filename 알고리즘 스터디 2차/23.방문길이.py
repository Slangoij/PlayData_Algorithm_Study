def solution(dirs):
    answer = 0

    hor_map = [[False] * 11 for _ in range(11)]
    ver_map = [[False] * 11 for _ in range(11)]
    now_pos = [5, 5]

    for move in dirs:
        if move == 'U' and now_pos[0]:
            if not ver_map[now_pos[0]-1][now_pos[1]]:
                ver_map[now_pos[0]-1][now_pos[1]] = True
                answer += 1
            now_pos[0] -= 1
        elif move == 'D' and now_pos[0] < 10:
            if not ver_map[now_pos[0]][now_pos[1]]:
                ver_map[now_pos[0]][now_pos[1]] = True
                answer += 1
            now_pos[0] += 1
        elif move == 'L' and now_pos[1]:
            if not hor_map[now_pos[0]][now_pos[1]-1]:
                hor_map[now_pos[0]][now_pos[1]-1] = True
                answer += 1
            now_pos[1] -= 1
        elif move == 'R' and now_pos[1] < 10:
            if not hor_map[now_pos[0]][now_pos[1]]:
                hor_map[now_pos[0]][now_pos[1]] = True
                answer += 1
            now_pos[1] += 1

    return answer


# dirs = "ULURRDLLU"
# dirs = "LLLLLL"
# dirs = "RRRRRR"
dirs = "UUUUUU"

print(solution(dirs))