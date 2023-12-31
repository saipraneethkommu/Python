# Add two matrices

# A matrix is a rectangular table of numbers. It is a collection of rows and columns.

# Write a program to add two matrices.

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]

# To add two matrices, we need to iterate through the rows and columns

# Initialize result matrix
result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

# iterate through rows

for i in range(len(A)):
    # iterate through columns
    for j in range(len(A[0])):
         result[i][j] = A[i][j] + B[i][j]

for r in result:
    print(r)