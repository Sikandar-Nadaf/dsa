

def longest_sub(ls):
    n = len(ls)
    dp = [1] * n ## dp[i] length of longest sub ending at i

    dp[0] = 1

    for i in range(n):
        for j in range(i):
            if ls[j] < ls[i]:
                dp[i] = max(dp[i],dp[j]+1)
                break

    return max(dp)




nums = [10,9,2,5,3,7,101,18]

print(longest_sub(nums))