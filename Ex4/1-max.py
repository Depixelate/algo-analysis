def my_max(arr, start, end):
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    max1 = my_max(arr, start, mid)
    max2 = my_max(arr, mid + 1, end)
    real_max = max1 if max1 > max2 else max2
    return real_max


if __name__ == "__main__":
    text = input("Enter some space separated numbers: ")
    nums = [int(num) for num in text.split()]
    print(f"{my_max(nums, 0, len(nums)-1)=}")

