def main():

    chessboard = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
    ]
    print(find_max_path(chessboard))

def find_max_path(chessboard):
    dp = []
    n = len(chessboard)
    m = len(chessboard[0])
    for i in range(n):
        dp.append(list())
        for j in range(m):
            dp[i].append((0, 0))

    for i in range(1, n):
        for j in range(1, m):
            current_value = chessboard[i][j]
            highest_value = value(dp[i - 1][j])
            previous_coordinates = (i - 1, j)
            if value(dp[i][j - 1]) > highest_value:
                highest_value = value(dp[i][j - 1])
                previous_coordinates = (i, j - 1)
            dp[i][j] = (previous_coordinates, highest_value + current_value)

    return greatest_path(dp)

def value(grid_selection):
    return grid_selection[1]

def coord(grid_selection):
    return grid_selection[0]

def greatest_path(dp):
    n = len(dp)
    m = len(dp[0])
    i = n - 1
    j = m - 1
    path = [(i, j)]
    while (i >= 2) or (j >= 2):
        coordinate = coord(dp[i][j])
        path.append(coordinate)
        i = coordinate[0]
        j = coordinate[1]
    return path

if __name__ == "__main__":
    main()