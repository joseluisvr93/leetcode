# You are given an array of prices where pirces[i] is the price of a stock on day i.
# You want to maximize your profit by choosing a single day to buy one stock and one choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. if you cannot make a profit, return 0.

def maxProfit(prices):
    max = prices[0]
    min = prices[0]
    res = 0

    for i in range(len(prices)):
        if prices[i] > max:
            max = prices[i]
            restemp = max-min
            if restemp > res:
                res = restemp
        if prices[i] < min:
            min = prices[i] 
            max = prices[i]

    return res 

prices = [1,2]
prices = [3,2,6,5,0,3]
print(maxProfit(prices))
