def combinations(n, k, nums, cur, num_stack):
    if len(num_stack) == k:
        print(num_stack)
        return
    if cur >= n:
        return
    
    combinations(n, k, nums, cur + 1, num_stack)
    num_stack.append(nums[cur])
    combinations(n, k, nums, cur + 1, num_stack)
    num_stack.pop()

def combinations_2(n, k, nums, cur, num_stack):
    if len(num_stack) == k:
        print(num_stack)
        return
    
    for i in range(cur, n - k + len(num_stack) + 1):
        num_stack.append(nums[i])
        combinations_2(n, k, nums, i+1, num_stack)
        num_stack.pop()

def to_dict(nums):
    num_dict = {}
    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict

def permutations(n, k, nums, num_stack):
    if len(num_stack) == k:
        print(num_stack)
        return
    
    for key in nums:
        if nums[key] == 0:
            continue
        
        num_stack.append(key)
        nums[key] -= 1
        permutations(n, k, nums, num_stack)
        nums[key] += 1
        num_stack.pop()


permutations(4, 3, to_dict([1,1,2,3]),[])
