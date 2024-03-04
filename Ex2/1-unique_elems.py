def unique_elems(arr):
    unique = []
    for i in range(len(arr)):
        if not containsMult(arr, arr[i]):
            unique.append(arr[i])
    return unique

def containsMult(arr, elem):
    count = 0
    for i in range(len(arr)):
        if arr[i] == elem:
            count += 1
    return count > 1

if __name__ == "__main__":
    text = input("Enter some space separated numbers: ")
    nums = [int(num) for num in text.split()]
    print(f"Unique nums: {unique_elems(nums)}")

