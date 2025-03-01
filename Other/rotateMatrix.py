# rotate a matrix 90 degrees

# with changing dimensions
from collections import deque


def rotateBy90(matrix):
    new_matrix = [[None for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    matrix_rows_num = len(matrix)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            new_matrix[c][matrix_rows_num-r-1] = matrix[r][c]
    
    return new_matrix

# for squared matrix
def transposeSquare(matrix):
    # trick: iterate over the upper triangle only
    for r in range(len(matrix)):
        for c in range(r, len(matrix[0])):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


# with square matrix
def rotateBy90Square(matrix):
    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    transposeSquare(matrix)
    print("transposed", matrix)
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix

if __name__ == "__main__":
    array = [[1,2],
             [3,4],
             [5,6]]
    print(array)

    rotated_array = rotateBy90(array)
    print(rotated_array)

    array2 = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    
    print(rotateBy90Square(array2))