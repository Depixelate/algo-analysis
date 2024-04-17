import math
# from collections import deque

# def is_valid(parenthesis:str):
#     count = 0
#     for char in parenthesis:
#         if char == '(':
#             count += 1
#         else:
#             count -= 1
#         if count < 0:
#             return False

#     return count == 0

# def min_parens_remove(parenthesis):
#     paren_queue = deque()
#     paren_queue.append((parenthesis, 0))
#     while len(paren_queue) > 0:
#         possibility, num_parens_removed = paren_queue.popleft()
#         if is_valid(possibility):
#             print(f"Number of parenthesis removed = {num_parens_removed}")
#             print(f"Output = {possibility}")
#             return
#         for i in range(len(possibility)):
#             new_possibility = possibility[:i] + possibility[i+1:]
#             if new_possibility not in paren_queue:
#                 paren_queue.append((new_possibility, num_parens_removed+1))


def is_valid(parens):
    count = 0
    for i in range(len(parens)):
        if parens[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
    
    return count == 0

def min_parens(parens, num_rem, min_num_rem):
    if num_rem >= min_num_rem:
        return math.inf, None
    
    if is_valid(parens):
        return num_rem, parens

    min_rem_parens = None
    for i in range(len(parens)):
        paren = parens.pop(i)
        possible_num_rem, possible_paren = min_parens(parens, num_rem + 1, min_num_rem)
        if possible_num_rem < min_num_rem:
            min_num_rem = possible_num_rem
            min_rem_parens = list(possible_paren)
        parens.insert(i, paren)
    return min_num_rem, min_rem_parens

if __name__ == "__main__":
    parens = input("Enter the parenthesis: ")
    num_rem, valid_parens = min_parens(list(parens), 0, math.inf)
    print(f"Number of parenthesis removed: {num_rem}")
    print(f"Valid Parenthesis: {''.join(valid_parens)}")

