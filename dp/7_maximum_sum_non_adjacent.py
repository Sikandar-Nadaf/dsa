# Problem — Maximum Sum of Non-Adjacent Elements
# 🔹 Problem Statement (Plain)

# Given an array of integers (can be positive or negative):

# Pick some elements

# No two picked elements are adjacent

# Maximize the total sum

# You are allowed to pick nothing.


def max_sum_non_adjacent(nums):

    n = len(nums)
    if n == 0:
       return 0
    if n == 1:
        return nums[0]
    
    dp = [0]*n
    dp[0] = max(0,nums[0])
    dp[1] = max(nums[0],nums[1])

    for i in range(2,n):
        dp[i] = max(nums[i]+dp[i-2],dp[i-1])

    return dp[-1]
    


nums = [3, 2, 5, 10, 7] 

print(max_sum_non_adjacent(nums))