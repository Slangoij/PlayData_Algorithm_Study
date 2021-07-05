def solution(board):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0 and board[i][j] == 'F':
                cnt += 1

    return cnt

# board = ["........","........","........","........","........","........","........","........"]
board = ["FFFFFFFF","FFFFFFFF","FFFFFFFF","FFFFFFFF","FFFFFFFF","FFFFFFFF","FFFFFFFF","FFFFFFFF"]
print(solution(board))