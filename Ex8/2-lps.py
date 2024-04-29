def lps(sequence):
    table = [[None for j in range(i+1)] for i in range(len(sequence))]
    lps_helper(sequence, table)
    seq_len, *_ = table[len(sequence) - 1][0]
    print(f"Max Sequence Length: {seq_len}")
    print(f"Sequence: {get_sequence(table, sequence, len(sequence) - 1, 0)}")


def lps_helper(sequence, table):
    for i in range(len(sequence)):
        for j in range(i, -1, -1):
            if sequence[i] == sequence[j]:
                if i == j:
                    len_inc = 1
                else:
                    len_inc = 2

                table[i][j] = (
                    get_ps_len(table, i - 1, j + 1) + len_inc,
                    i - 1,
                    j + 1,
                    True,
                )
                continue

            up_entry = (
                get_ps_len(table, i - 1, j),
                i - 1,
                j,
                False,
            )

            right_entry = (
                get_ps_len(table, i, j + 1),
                i,
                j + 1,
                False,
            )

            table[i][j] = max(
                up_entry, right_entry, key=lambda entry: entry[0]
            )


def get_ps_len(table, i, j):
    if i < 0:
        return 0

    if j > i:
        return 0

    return table[i][j][0]


def get_sequence(table, sequence, i, j):
    if i < 0:
        return ""

    if j > i:
        return ""

    _, next_i, next_j, part_of_palindrome = table[i][j]

    if part_of_palindrome:
        return sequence[i] if i == j else sequence[j] + get_sequence(table, sequence, next_i, next_j) + sequence[i]
    
    return get_sequence(table, sequence, next_i, next_j)

if __name__ == "__main__":
    sequence = input("Enter a sequence: ")
    lps(sequence)
