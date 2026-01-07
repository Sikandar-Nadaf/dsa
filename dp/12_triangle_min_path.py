





def traingle_path(tree):
    
    n = len(tree)

    dp = [[0]*(i+1)for i in range(n)]

    dp[0][0] = tree[0][0]

    for i in range(1,n):
        for j in range(i+1):
            if j == 0: ## LEFT EDGE,
                dp[i][j] = dp[i-1][j] + tree[i][j]
            elif j == i: ## Right Edge
                dp[i][j] = dp[i-1][j-1] + tree[i][j]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + tree[i][j]

    return min(dp[-1])




triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]


print(traingle_path(triangle))

