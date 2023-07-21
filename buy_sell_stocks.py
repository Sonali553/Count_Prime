def buyAndSell_Stocks(lst):
    l =0
    r = 1
    maxProfit = 0
    while(r < len(lst)):
        if lst[l] < lst[r]:
            maxProfit = max(maxProfit, lst[r] - lst[l])
        else:
            l = r
        r += 1
    return maxProfit
print(buyAndSell_Stocks([1, 2]))
print(buyAndSell_Stocks([1, 4, 5, 2, 4]))