#!/usr/bin/env python3

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    min_price = prices[0]
    min_index = 0
    for index, element in enumerate(prices):
        if element < min_price:
            min_pric
