# how to shift a pointer based off of a condition
# use two pointers the difference in values

def maxProfit(prices):
        l, res = 0, 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))