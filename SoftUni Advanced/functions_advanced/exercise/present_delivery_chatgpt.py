def print_neighborhood(neighborhood):
    for row in neighborhood:
        print(''.join(row))


def find_santa_position(neighborhood):
    for i in range(len(neighborhood)):
        for j in range(len(neighborhood[i])):
            if neighborhood[i][j] == 'S':
                return i, j


def main():
    m = int(input())
    n = int(input())

    neighborhood = [list(input()) for _ in range(n)]

    commands = []
    for _ in range(n):
        commands.append(input())

    nice_kids_count = sum(row.count('V') for row in neighborhood)
    santa_row, santa_col = find_santa_position(neighborhood)

    for command in commands:
        neighborhood[santa_row][santa_col] = '-'

        if command == 'up':
            santa_row -= 1
        elif command == 'down':
            santa_row += 1
        elif command == 'left':
            santa_col -= 1
        elif command == 'right':
            santa_col += 1

        if 0 <= santa_row < n and 0 <= santa_col < n:
            if neighborhood[santa_row][santa_col] == 'V':
                m -= 1
                nice_kids_count -= 1
                neighborhood[santa_row][santa_col] = '-'
            elif neighborhood[santa_row][santa_col] == 'C':
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = santa_row + dr, santa_col + dc
                    if 0 <= r < n and 0 <= c < n and neighborhood[r][c] == 'V':
                        m -= 1
                        nice_kids_count -= 1
                        neighborhood[r][c] = '-'

        if m == 0:
            break

    print_neighborhood(neighborhood)

    if nice_kids_count == 0:
        print(f"Good job, Santa! {sum(row.count('V') for row in neighborhood)} happy nice kid/s.")
    else:
        print(f"No presents for {nice_kids_count} nice kid/s.")

    if m == 0:
        print("Santa ran out of presents!")


if __name__ == "__main":
    main()

