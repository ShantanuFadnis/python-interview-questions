"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

"""

def min_cost(matrix, N, k):
    previous_house = 0
    previous_house_index = -1
    previous_house_next = 0

    for i in range(N):
        current_house = k
        current_house_next = k
        current_house_index = 0
        
        for j in range(k):
            if previous_house_index == j:
                matrix[i][j] += previous_house_next
            else:
                matrix[i][j] += previous_house
            
            if current_house_next > matrix[i][j]:
                current_house_next = current_house
                current_house = matrix[i][j]
                current_house_index = j
            elif current_house_next > matrix[i][j]:
                current_house_next = matrix[i][j]

        previous_house = current_house
        previous_house_index = current_house_index
        previous_house_next = current_house_next

    return min(matrix[N-1])

matrix1 = [[7, 3, 8, 6, 1, 2], [5, 6, 7, 2, 4, 3], [10, 1, 4, 9, 7, 6]]
matrix2 = [[7, 3, 8, 6, 1, 2], [5, 6, 7, 2, 4, 3], [10, 1, 4, 9, 7, 6], [10, 1, 4, 9, 7, 6]]

matrix3 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
matrix4 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

print(min_cost(matrix1, 3, 6))
print(min_cost(matrix2, 4, 6))
print(min_cost(matrix3, 2, 6))
print(min_cost(matrix4, 3, 6))
