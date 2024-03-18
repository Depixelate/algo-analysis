def merge_count(nums, start, end):
    if start == end:
        return 0
    count = 0
    mid = (start + end) // 2
    count += merge_count(nums, start, mid)
    count += merge_count(nums, mid + 1, end)
    count += merge(nums, start, end)

    return count


def merge(nums, start, end):
    tot_len = end - start + 1
    aux = [0] * (tot_len)
    count = 0
    mid = (start + end) // 2
    i, j = 0, 0
    while i + j < tot_len:
        if mid + 1 + j > end or (
            start + i < mid + 1 and nums[start + i] <= nums[mid + 1 + j]
        ):
            aux[i + j] = nums[start + i]
            i += 1
        else:
            aux[i + j] = nums[mid + 1 + j]
            count += mid + 1 - start - i
            j += 1
    for i in range(start, end + 1):
        nums[i] = aux[i - start]

    return count


def count_inversions(nums):
    return merge_count(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    print(f"{count_inversions([3, 2, 8, 1])=}")
