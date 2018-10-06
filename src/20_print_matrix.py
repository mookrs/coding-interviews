def print_matrix(matrix):
    if matrix is None:
        return

    rows = len(matrix)
    columns = len(matrix[0])
    start = 0
    while rows > start * 2 and columns > start * 2:
        print_matrix_in_circle(matrix, columns, rows, start)
        start += 1

    print()


def print_matrix_in_circle(matrix, columns, rows, start):
    end_x = columns - 1 - start
    end_y = rows - 1 - start

    # 从左到右打印一行
    for i in range(start, end_x + 1):
        number = matrix[start][i]
        print(number, ' ', end='')

    # 从上到下打印一行
    if start < end_y:
        for i in range(start + 1, end_y + 1):
            number = matrix[i][end_x]
            print(number, ' ', end='')

    # 从右到左打印一行
    if start < end_x and start < end_y:
        for i in range(end_x - 1, start - 1, -1):
            number = matrix[end_y][i]
            print(number, ' ', end='')

    # 从下到上打印一行
    if start < end_x and start < end_y - 1:
        for i in range(end_y - 1, start, -1):
            number = matrix[i][start]
            print(number, ' ', end='')


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [[1], [2], [3], [4], [5]]
matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print_matrix(matrix)
print_matrix(matrix2)
print_matrix(matrix3)
