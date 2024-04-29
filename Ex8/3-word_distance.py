import enum


class Edit(enum.Enum):
    INSERT = 0
    UPDATE = 1
    DELETE = 2
    NONE = 3


def min_edit_dist(actual, target):
    table = [[None for j in range(len(target))] for i in range(len(actual))]
    min_edit_dist_helper(actual, target, table)
    num_edits, *_ = table[0][0]
    print(f"Minimum Number of edits: {num_edits}")
    print()
    print("Edits:")
    print_edits(table, actual, target, 0, 0, 0, actual)


def min_edit_dist_helper(actual, target, table):
    for i in range(len(actual) - 1, -1, -1):
        for j in range(len(target) - 1, -1, -1):
            if actual[i] == target[j]:
                table[i][j] = (
                    get_edit_dist(table, i + 1, j + 1, len(actual), len(target)),
                    i + 1,
                    j + 1,
                    Edit.NONE,
                )
                continue

            update_entry = (
                get_edit_dist(table, i + 1, j + 1, len(actual), len(target)) + 1,
                i + 1,
                j + 1,
                Edit.UPDATE,
            )

            insert_entry = (
                get_edit_dist(table, i, j + 1, len(actual), len(target)) + 1,
                i,
                j + 1,
                Edit.INSERT,
            )

            delete_entry = (
                get_edit_dist(table, i + 1, j, len(actual), len(target)) + 1,
                i + 1,
                j,
                Edit.DELETE,
            )

            table[i][j] = min(
                insert_entry, delete_entry, update_entry, key=lambda entry: entry[0]
            )


def get_edit_dist(table, i, j, len_actual, len_target):
    if i >= len_actual:
        return len_target - j

    if j >= len_target:
        return len_actual - i

    return table[i][j][0]


def print_edits(table, actual, target, i, j, offset, cur):
    if i >= len(actual) and j >= len(target):
        return

    if i >= len(actual):
        print()
        print(f"Insert \"{target[j:]}\" at end")
        new_cur = cur + target[j:]
        print(f"\"{cur}\"->\"{new_cur}\"")
        return

    if j >= len(target):
        print()
        print(f"Delete \"{cur[i+offset:]}\" from end")
        new_cur = cur[:i+offset]
        print(f"\"{cur}\"->\"{new_cur}\"")
        return

    _, next_i, next_j, edit_type = table[i][j]

    match edit_type:
        case Edit.UPDATE:
            print()
            print(f"Update '{cur[i+offset]}' at index {i+offset} to '{target[j]}'")
            new_cur = cur[: i + offset] + target[j] + cur[i + offset + 1 :]
            print(f"\"{cur}\"->\"{new_cur}\"")
            cur = new_cur
        case Edit.INSERT:
            print()
            print(f"Insert '{target[j]}' in front of '{cur[i+offset]}' at index {i+offset}")
            new_cur = cur[: i + offset] + target[j] + cur[i + offset :]
            print(f"\"{cur}\"->\"{new_cur}\"")
            cur = new_cur
            offset += 1
        case Edit.DELETE:
            print()
            print(f"Delete '{cur[i+offset]}' at index {i+offset}")
            new_cur = cur[:i+offset] + cur[i+offset+1:]
            print(f"\"{cur}\"->\"{new_cur}\"")
            cur = new_cur
            offset -= 1

    print_edits(table, actual, target, next_i, next_j, offset, cur)

if __name__ == "__main__":
    actual = input("Enter the current word: ")
    target = input("Enter the target word: ")
    min_edit_dist(actual, target)
