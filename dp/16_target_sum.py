




def target_sum_ways(nums, t):
    total = sum(nums)

    if abs(t) > total or (t + total) % 2 != 0:
        return 0

    p = (t + total) // 2

    dp = [[0] * (p + 1) for _ in range(len(nums) + 1)]
    dp[0][0] = 1

    for i in range(1, len(nums) + 1):
        for j in range(p + 1):
            dp[i][j] = dp[i-1][j]
            if j >= nums[i-1]:
                dp[i][j] += dp[i-1][j - nums[i-1]]

    return dp[-1][p]







nums = [1,2,3]
print(target_sum_ways(nums,0))