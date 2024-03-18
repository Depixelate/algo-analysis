import random
import time

def increment_sort(elems, increment):
    for i in range(increment, len(elems)):
        #print(f"{i=}")
        for j in range(i, increment - 1, -increment):
            if elems[j] < elems[j - increment]:
                elems[j], elems[j - increment] = elems[j - increment], elems[j]
            else:
                break


def insertion_sort(elems):
    increment_sort(elems, 1)

def unique_rand(n):
    rands = list(range(n))
    random.shuffle(rands)
    return rands

unsorted_elems = unique_rand(100000)
ascending_elems = sorted(unsorted_elems)
descending_elems = sorted(unsorted_elems, reverse=True)

ascending_start_ns = time.process_time_ns()
insertion_sort(ascending_elems)
ascending_end_ns = time.process_time_ns()
ascending_time = (ascending_end_ns - ascending_start_ns)/10**9
print(f"{ascending_time=}")

descending_start_ns = time.process_time_ns()
insertion_sort(descending_elems)
descending_end_ns = time.process_time_ns()
descending_time = (descending_end_ns - descending_start_ns)/10**9
print(f"{descending_time=}")

unsorted_start_ns = time.process_time_ns()
insertion_sort(unsorted_elems)
unsorted_end_ns = time.process_time_ns()
unsorted_time = (unsorted_end_ns - unsorted_start_ns)/10**9
print(f"{unsorted_time=}")

with open("results.txt", "a", encoding="utf-8") as f:
    f.write(f"{ascending_time=}, {descending_time=}, {unsorted_time=}")