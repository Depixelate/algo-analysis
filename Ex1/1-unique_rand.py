import random


def unique_rand(n):
    rands = list(range(n))
    random.shuffle(rands)
    return rands


if __name__ == "__main__":
    # start = int(input("Enter the start for the range of random numbers: "))
    # end = int(input("Enter the end for the range of random numbers(inclusive): "))
    n = int(input("Enter the no. random nums you want to generate: "))
    nums = unique_rand(n)
    print(f"The numbers: {nums}")
