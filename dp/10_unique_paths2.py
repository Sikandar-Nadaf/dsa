



def unique_paths_2(grid):

    m = len(grid)
    n = len(grid[0])

    dp = [[0] *n for i in range(m)]
    
    dp[0][0]=1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j]+=dp[i-1][j]
                if j > 0:
                    dp[i][j]+=dp[i][j-1]

    print(dp)
    return dp[m-1][n-1]


obstacleGrid = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]


print(unique_paths_2(obstacleGrid))