# The famous - You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    buy = 0
    sell = 1
    max_profit = prices[1] - prices[0]
    new_sell = 2
    new_buy = 1
    while(new_sell < len(prices)):
        if prices[new_sell] >= prices[sell]:
            sell = new_sell
            while(new_buy<sell):
                if prices[new_buy] <= prices[buy]:
                    buy = new_buy
                new_buy += 1
            max_profit = max(max_profit, prices[sell]-prices[buy])
        if prices[new_buy] <= prices[buy]:
            buy = new_buy
        new_sell+=1
        new_buy+=1
    return max_profit if max_profit>0 else 0

def maxProfitCleaner(prices):
    buy, sell = 0, 1
    max_profit = max(0, prices[1]-prices[0])
    while (sell < len(prices)):
        # if prices go up, lets check the new profit
        if prices[sell] > prices[buy]:
            max_profit = max(max_profit, prices[sell]-prices[buy])
            sell+=1
        # prices went down, update the buying time
        else:
            buy = sell
            sell+=1
    return max_profit

# TODO: follow-up: what if you can do it twice?
# TODO: fix the bug here... i think i need to find for each half of the array..
def twoTimesBuySell(prices):
    buy, sell = 0, 1
    max_profit1 = max(0, prices[1]-prices[0])
    max_profit2 = 0
    flag = True
    while (sell < len(prices)):
        # if prices go up, lets check the new profit
        if prices[sell] > prices[buy]:
            if flag:
                max_profit1 = max(max_profit1, prices[sell]-prices[buy])
            else:
                max_profit2 = max(max_profit2, prices[sell]-prices[buy])
            sell+=1
        # prices went down, update the buying time
        else:
            buy = sell
            sell+=1
            if max_profit1<max_profit2:
                flag=True
            else:
                flag=False
    return max_profit1, max_profit2


if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))

    print(maxProfitCleaner([7,1,5,3,6,4]))
    print(maxProfitCleaner([7,6,4,3,1]))
    print(maxProfitCleaner([1,8,4,3,2,10]))

    print(twoTimesBuySell([1,8,4,3,2,10]))
        

    