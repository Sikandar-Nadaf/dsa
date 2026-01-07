

def subset_sum(nums,s):
    
    dp = [[False]*(s+1) for i in range(len(nums)+1)]
    dp[0][0] = True

    for i in range(1,len(nums)+1):
        for j in range(s+1):
            dp[i][j] = dp[i-1][j] 
            if j >= nums[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]

    print(dp)
    return dp[-1][s]






nums = [3, 34, 4, 12, 5, 2]
T = 9

print(subset_sum(nums,T))
    