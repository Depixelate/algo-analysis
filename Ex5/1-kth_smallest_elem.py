import random
import time

def increment_sort(elems, increment):
    for i in range(increment, len(elems)):
        for j in range(i, increment - 1, -increment):
            if elems[j] < elems[j - increment]:
                elems[j], elems[j - increment] = elems[j - increment], elems[j]
            else:
                break


def insertion_sort(elems):
    increment_sort(elems, 1)

def partition(arr, start, end, pivot_ind):
    arr[pivot_ind], arr[start] = arr[start], arr[pivot_ind]
    pivot_ind = start
    for i in range(pivot_ind, end + 1):
        if arr[i] < arr[pivot_ind]:
            arr[i], arr[pivot_ind + 1] = arr[pivot_ind + 1], arr[i]
            arr[pivot_ind], arr[pivot_ind + 1] = arr[pivot_ind + 1], arr[pivot_ind]
            pivot_ind += 1
    return pivot_ind

def k_smallest(arr, k, start, end):
    print(f"{start=}, {end=}")
    if start == end:
        return arr[start]
    pivot_ind = partition(arr, start, end, random.randint(start, end))
    if pivot_ind == k - 1:
        return arr[pivot_ind]
    if pivot_ind > k - 1:
        return k_smallest(arr, k, start, pivot_ind - 1)
    return k_smallest(arr, k, pivot_ind + 1, end)

if __name__ == "__main__":
    seed = time.time_ns()
    #random.seed(seed)
    #print(f"{seed=}")
    nums_str = input("Enter comma separated numbers: ")
    nums = [int(num_str) for num_str in nums_str.split(',')]
    k = int(input("Enter k: "))
    k_small = k_smallest(nums, k, 0, len(nums) - 1)
    print(f"K-th smallest elem: {k_small}")
