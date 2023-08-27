#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == floar('inf'):
        return -1
    return dp[total]
