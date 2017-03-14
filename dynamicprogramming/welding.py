
def main():
    steel_pieces = [1, 2, 3, 4, 5, 6]
    print(minimum_weld_price(steel_pieces))

def minimum_weld_price(steel_piece_weights):
    n = len(steel_piece_weights)
    dp = list()
    for i in range(n):
        dp.append(list())
        for j in range(n):
            dp[i].append(0)

    # for level in range(2, n):
    #     for i in range(n - level + 1):
    #         j = i + level - 1
    #         for k in range(i, j):
    #             min_cost = dp[i][j - 1]
    #             if dp[i + 1][j] < min_cost:
    #                 min_cost = dp[i + 1][j]
    #             dp[i][j] = min_cost + steel_pieces[k]
    for i in range(n):
        for j in range(n):
            if i is not j: # Can't weld a piece to itself
                min_cost = steel_piece_weights[i]
                if steel_piece_weights[j] < min_cost:
                    min_cost = steel_piece_weights[j]
                dp[i][j] = min_cost



if __name__ == "__main__":
    main()