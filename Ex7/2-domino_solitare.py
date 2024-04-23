def max_score(board):
    score = [0 for i in range(len(board[0]))]
    for i in range(len(board[0])):
        vert_score = calc_score(board[0][i], board[1][i])
        vert_score += get_score(score, i - 1)
        horiz_score = 0
        if i > 0:
            horiz_score = calc_score(board[0][i], board[0][i-1]) + calc_score(board[1][i], board[1][i-1])
            horiz_score += get_score(score, i - 2)
        score[i] = max(vert_score, horiz_score)
    return score[len(board[0])-1]

def calc_score(a, b):
    return max(a, b) - min(a, b)

def get_score(score, index):
    if index < 0:
        return 0
    return score[index]

if __name__ == "__main__":
    row1 = [
        int(num_str) 
        for num_str in input(
            "Enter space separated numbers for the first row of the board: "
            ).split()
    ]

    row2 = [
        int(num_str)
        for num_str in input(
            "Enter space separated numbers for the second row of the board: "
        ).split()
    ]
    board = [row1, row2]
    score = max_score(board)
    print(f"Max score: {score}")

