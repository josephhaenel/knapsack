'''

File Name: Knapsack.py
Compile: py Knapsack.py

Purpose: Implimentation of the O(nW) matrix based dynamic programming algorithm to solve the Knapsack problem
Author: Joseph Haenel
Creation Date: 04/19/2023

Last Edited Date: 04/23/2023

'''


def read_input(file_name):
    with open(file_name, 'r') as file:
        n, W = map(int, file.readline().strip().split())
        items = []
        for line in file:
            weight, value = map(int, line.strip().split())
            items.append((weight, value))
    return n, W, items


def knapsack(n, W, items):
    # Initialize the matrix
    matrix = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill the matrix
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for j in range(W + 1):
            if weight <= j:
                matrix[i][j] = max(
                    matrix[i - 1][j], matrix[i - 1][j - weight] + value)
            else:
                matrix[i][j] = matrix[i - 1][j]

    # Backtrack to find the optimal solution
    optimal_items = []
    i, j = n, W
    while i > 0 and j > 0:
        if matrix[i][j] != matrix[i - 1][j]:
            optimal_items.append(i)
            j -= items[i - 1][0]
        i -= 1

    return matrix[-1][-1], optimal_items


def main():
    n, W, items = read_input('knapsack.txt')
    total_value, optimal_items = knapsack(n, W, items)
    print(
        f"The optimal Knapsack solution has total value {total_value} and involves items {sorted(optimal_items)}.")


if __name__ == "__main__":
    main()
