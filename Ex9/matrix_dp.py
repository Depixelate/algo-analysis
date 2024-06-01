import math
def matrix_dp(mats):
    table = [[None for j in range(len(mats))] for i in range(len(mats))]
    
    for l in range(len(mats)):
        for i in range(len(mats) - l):
            j = i + l
            if i == j:
                table[i][j] = 0, i
                continue
            min_cost = math.inf
            min_k = -1
            for k in range(i, j):
                cost = table[i][k][0] + table[k+1][j][0] + mats[i][0] * mats[k][1] * mats[j][1]
                if cost < min_cost:
                    min_cost = cost
                    min_k = k
            table[i][j] = min_cost, min_k
    
    print_mats(table, 0, len(mats) - 1, [0])
    print()
    return table[0][len(mats)-1][0]
    

def print_mats(table, i, j, count):
    if i == j:
        print(chr(ord('A') + count[0]), end='')
        count[0] += 1
        return
    k = table[i][j][1]
    print('(', end='')
    print_mats(table, i, k, count)
    print_mats(table, k+1, j, count)
    print(')', end='')

mats = [(3,2), (2,6), (6,4), (4,5), (5,2)]    
print(f"Cost: {matrix_dp(mats)}")
    