"""
matrix manipulation
rotate matrix clockwise 90 degree. Not transpose!
input: 2d array
output: None. cuz it will be the same array 
clarification: no edge case
"""

"""
1. reversing matrix
2. flip non diagonal entries
"""

def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
