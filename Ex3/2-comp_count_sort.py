def comparison_count_sort(nums):
	count = [0] * len(nums)
	nums_sorted = [0] * len(nums)
	for i in range(len(nums) - 1):
		for j in range(i + 1, len(nums)):
			if nums[i] > nums[j]:
				count[i] += 1
			elif nums[i] <= nums[j]:
				count[j] += 1
	for i in range(len(nums)):
		nums_sorted[count[i]] = nums[i]
	return nums_sorted

if __name__ == "__main__":
	print(f"{comparison_count_sort([3, 2, 9, 4, 1, 7])=}")
	
