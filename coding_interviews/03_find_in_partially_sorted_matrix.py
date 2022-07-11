def find(matrix, number):
    if not matrix:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] < number:
            row += 1
        elif matrix[row][col] > number:
            col -= 1
        else:
            return True

    return False


matrix = [[1, 2, 3], [2, 3, 6], [3, 6, 7]]
number = 6
print(find(matrix, number))
