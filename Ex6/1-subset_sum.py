def subset_sum(target_left, used, nums, start_ind):
    if target_left == 0:
        print(used)
    
    if target_left <= 0:
        return
    
    for i in range(start_ind, len(nums)):
        used.append(nums[i])
        subset_sum(target_left - nums[i], used, nums, i+1)
        used.pop()
    

nums_str = input("Enter a comma separated set of numbers: ")
nums = [int(num_str) for num_str in nums_str.split(",")]
target = int(input("Enter a target: "))
print(f"The subsets of {nums} which add up to {target}: ")
subset_sum(target, [], nums, 0)
    

