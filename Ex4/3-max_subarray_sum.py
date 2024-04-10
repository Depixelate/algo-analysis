def max_subarray_sum(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2
    max1 = max_subarray_sum(arr, start, mid)
    max2 = max_subarray_sum(arr, mid + 1, end)

    max_left = 0
    cum_left = 0
    for i in range(mid, start - 1, -1):
        cum_left += arr[i]
        if cum_left > max_left:
            max_left = cum_left

    max_right = 0
    cum_right = 0
    for i in range(mid + 1, end + 1):
        cum_right += arr[i]
        if cum_right > max_right:
            max_right = cum_right

    max3 = max_left + max_right

    return max(max1, max2, max3)


if __name__ == "__main__":
    text = input("Enter some space separated numbers: ")
    nums = [int(num) for num in text.split()]
    print(f"{max_subarray_sum(nums, 0, len(nums)-1)}")
    