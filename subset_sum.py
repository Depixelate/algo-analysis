def subset_sum(nums, target, cur, num_stack):
    if target == 0:
        print(num_stack)
        return
    if cur >= len(nums):
        return
    if target < 0:
        return
    
    subset_sum(nums, target, cur + 1, num_stack)
    num_stack.append(nums[cur])
    subset_sum(nums, target - nums[cur], cur + 1, num_stack)
    num_stack.pop()

subset_sum([1, 2, 3, 4, 5, 6], 12, 0, [])