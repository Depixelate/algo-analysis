def is_valid(queen_pos, row, col):
    for q_row, q_col in queen_pos:
        if col == q_col:
            return False
        
        if abs(q_row - row) == abs(q_col - col):
            return False
    return True

def nqueens(n, queen_pos = []):
    if len(queen_pos) == n:
        print(queen_pos)
        return
    
    row = len(queen_pos)
    for col in range(n):
        if not is_valid(queen_pos, row, col):
            continue
        queen_pos.append((row, col))
        nqueens(n, queen_pos)
        queen_pos.pop()
    
nqueens(8)