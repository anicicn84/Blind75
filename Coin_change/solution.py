
def countChange(denominations, total):
    dp = [0 for i in range(0, total+1)]
    dp[0] = 1
    for coin in denominations:
        for diff_total_coin in range(coin, total+1):
            dp[diff_total_coin] += dp[diff_total_coin - coin]
    return dp[total]

denominations = [1, 2, 3]
total = 5
assert(countChange(denominations, total) == 5)