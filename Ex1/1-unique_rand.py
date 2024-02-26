import random;
def unique_rand(start, end, n):
	nums = {}
	while len(nums) < n:
		nums[random.randint(start, end)]=None
	return list(nums.keys())

def unique_rand_2(n):
	return random.shuffle(range(n))

if __name__ == "__main__":
	start = int(input("Enter the start for the range of random numbers: "))
	end = int(input("Enter the end for the range of random numbers(inclusive): "))
	n = int(input("Enter the no. random nums you want to generate: "))
	nums = unique_rand(start, end, n)
	print(f"The numbers: {nums}")

