def calc_sum(n):
    return n * (n+1) * (n+2) / 6

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"Sum: {calc_sum(n)}")