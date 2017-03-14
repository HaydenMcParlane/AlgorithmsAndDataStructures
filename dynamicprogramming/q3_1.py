def main():
    # matrix_dimensions = (7,10,9,5,12,6)
    matrix_dimensions = (30,1,40,10,25)
    print(optimal_matrix_chain_multiplication(matrix_dimensions))

# TODO: Return to later
def optimal_matrix_chain_multiplication(matrix_dimensions):
    dp = []
    n = len(matrix_dimensions) - 1
    for i in range(n):
        dp.append(list())
        for j in range(n):
            dp[i].append(0)

    for level in range(2, n):
        for i in range(n - level + 1):
            j = i + level - 1
            for k in range(i, j):
                # complexity = dp[i][k] + dp[k+1][j] +
                pass

if __name__ == "__main__":
    main()