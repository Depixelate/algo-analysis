def max_subarray_sum(nums):
    aux = [0] * len(nums)
    prev = 0
    for i, num in enumerate(nums):
        aux[i] = prev + num
        prev = aux[i]
    
    print(f"{aux=}")
    
    cur_lowest = 0
    cur_max = 0

    for num in aux:
        cur_sum = num - cur_lowest
        if cur_sum > cur_max:
            cur_max = cur_sum
        if num < cur_lowest:
            cur_lowest = num
    
    return cur_max


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"{max_subarray_sum(nums)}")
