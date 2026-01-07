




def equal_subset(nums):
    
    s = sum(nums)
    if s%2!=0:
        return False
    s = s//2

    dp  = [[False]*(s+1) for i in range(len(nums)+1)]

    dp[0][0] = True # each cell denotes if we can for sum s with n items

    for i in range(1,len(nums)+1):
        for j in range(s+1):
            dp[i][j] = dp[i-1][j]  # dont select this number
            if j >= nums[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]

    return dp[-1][s]







nums = [1, 5, 11, 5]
print(equal_subset(nums))