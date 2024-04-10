from collections import deque

def is_valid(parenthesis:str):
    count = 0
    for char in parenthesis:
        if char == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
        
    return count == 0

def min_parens_remove(parenthesis):
    paren_queue = deque()
    paren_queue.append((parenthesis, 0))
    while len(paren_queue) > 0:
        possibility, num_parens_removed = paren_queue.popleft()
        if is_valid(possibility):
            print(f"Number of parenthesis removed = {num_parens_removed}")
            print(f"Output = {possibility}")
            return
        for i in range(len(possibility)):
            new_possibility = possibility[:i] + possibility[i+1:]
            if new_possibility not in paren_queue:
                paren_queue.append((new_possibility, num_parens_removed+1))


parens = input("Enter the parenthesis: ")
min_parens_remove(parens)
