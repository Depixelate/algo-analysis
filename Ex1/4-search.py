import random
import time

def unique_rand(n):
    rands = list(range(n))
    random.shuffle(rands)
    return rands

def rec_binary_search(elems, elem, start, end):
    if end < start:
        return -1
    mid_ind = (start + end)//2
    if elem == elems[mid_ind]:
        return mid_ind
    if elem < elems[mid_ind]:
        return rec_binary_search(elems, elem, start, mid_ind-1)
    return rec_binary_search(elems, elem, mid_ind + 1, end)

def iter_binary_search(elems, elem):
    start, end = 0, len(elems) - 1
    while end >= start:
        mid_ind = (start + end)//2
        if elem == elems[mid_ind]:
            return mid_ind
        if elem < elems[mid_ind]:
            end = mid_ind - 1 
        else:
            start = mid_ind + 1
    return -1

nums = unique_rand(100000)
iter_start = time.perf_counter_ns()
iter_binary_search(nums, -1)
iter_end = time.perf_counter_ns()
iter_time = (iter_end - iter_start)/1000
print(f"{iter_time=}us")
rec_start = time.perf_counter_ns()
rec_binary_search(nums, -1, 0, len(nums)-1)
rec_end = time.perf_counter_ns()
rec_time = (rec_end - rec_start)/1000
print(f"{rec_time=}us")