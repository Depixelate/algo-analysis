import matplotlib.pyplot as plt
import time
import random


def unique_rand(n):
    rands = list(range(n))
    random.shuffle(rands)
    return rands

def bucket_sort(elems, power, radix):
    digit_buckets = [[] for i in range(radix)]
    ended = True
    
    for elem in elems:
        digit = (elem // power) % radix
        if digit != 0:
            ended = False
        digit_buckets[digit].append(elem)
    
    k = 0
    for bucket in digit_buckets:
        for elem in bucket:
            elems[k] = elem
            k+=1
    return ended
    

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
        digit_counts[digit] += 1

    for i in range(len(elems)):
        elems[i] = digit_sorted_elems[i]

    return is_radix_too_big


def radix_sort(elems, radix):
    power = 1
    while not bucket_sort(elems, power, radix):
        power *= radix


def increment_sort(elems, increment):
    for i in range(increment, len(elems)):
        for j in range(i, increment - 1, -increment):
            if elems[j] < elems[j - increment]:
                elems[j], elems[j - increment] = elems[j - increment], elems[j]
            else:
                break


def insertion_sort(elems):
    increment_sort(elems, 1)


def shell_sort(elems):
    increment = int(len(elems) / 2)
    while increment > 0:
        increment_sort(elems, increment)
        increment = int(increment / 2)


if __name__ == "__main__":
    ns = [10, 1000, 2000, 5000, 100000]
    timeRadix, timeShell, timeInsertion = [], [], []
    for i in ns:
        #print(f"Now considering arrays of size {i}: ")
        nums = unique_rand(i)
        nums1, nums2, nums3 = list(nums), list(nums), list(nums)
        start = time.perf_counter()
        radix_sort(nums1, 256)
        timeRadix.append(time.perf_counter() - start)
        start = time.perf_counter()
        shell_sort(nums2)
        timeShell.append(time.perf_counter() - start)
        start = time.perf_counter()
        insertion_sort(nums3)
        timeInsertion.append(time.perf_counter() - start)
        #print(f"{timeInsertion[-1]=}, {timeRadix[-1]=}, {timeShell[-1]=}")

    fig1 = plt.plot(ns, timeRadix, label="radix")
    fig2 = plt.plot(ns, timeShell, label="shell")
    fig3 = plt.plot(ns, timeInsertion, label="insertion")
    plt.legend()
    plt.xscale("log")
    plt.yscale("log")
    plt.savefig("sorts_compared.png")
    # fig2.savefig("2.png")
    # fig3.savefig("3.png")
