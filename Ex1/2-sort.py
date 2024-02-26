import unique_rand as ur
import matplotlib.pyplot as plt
import time

def count_sort(elems, radix, radix_to_n):
	digit_sorted_elems = [0 for i in range(len(elems))]
	digit_counts = [0 for i in range(radix)]
	is_radix_too_big = True
	
	for elem in elems:
		digit = int(elem / radix_to_n) % radix
		if digit != 0:
			is_radix_too_big = False
		digit_counts[digit] += 1
	
	cum_sum = 0
	for i in range(len(digit_counts)):
		count = digit_counts[i]
		digit_counts[i] = cum_sum
		cum_sum += count
	
	for elem in elems:
		digit = int(elem / radix_to_n) % radix
		digit_sorted_elems[digit_counts[digit]] = elem
		digit_counts[digit]+=1
	
	for i in range(len(elems)):
		elems[i] = digit_sorted_elems[i]
	
	return is_radix_too_big

def radix_sort(elems, radix):
	radix_to_n = 1
	while not count_sort(elems, radix, radix_to_n):
		radix_to_n *= radix
		
def increment_sort(elems, increment):
	for i in range(increment, len(elems)):
		for j in range(i, increment-1, -increment):
			 if elems[j] < elems[j-increment]:
			 	elems[j], elems[j-increment] = elems[j-increment], elems[j]
			 else:
			 	break

def insertion_sort(elems):
	increment_sort(elems, 1)

def shell_sort(elems):
	increment = int(len(elems)/2)
	while increment > 0:
		increment_sort(elems, increment)
		increment = int(increment/2)

if __name__ == "__main__":
	ns = list(range(1, 1000))	
	times1, times2, times3 = [], [], []
	for i in ns:
		nums = ur.unique_rand(i)
		nums1, nums2, nums3 = list(nums), list(nums), list(nums)
		start = time.perf_counter()
		radix_sort(nums1, 256)
		times1.append(time.perf_counter()-start)
		start = time.perf_counter()
		shell_sort(nums2)
		times2.append(time.perf_counter()-start)		
		start = time.perf_counter()
		insertion_sort(nums3)
		times3.append(time.perf_counter()-start)
	fig1 = plt.plot(ns, times1, label="radix")
	fig2 = plt.plot(ns, times2, label="shell")
	fig3 = plt.plot(ns, times3, label="insertion")
	plt.legend()
	plt.savefig("4.png")
	#fig2.savefig("2.png")
	#fig3.savefig("3.png")

