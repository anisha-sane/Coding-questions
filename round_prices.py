'''
Created on 15-Oct-2018

@author: User
'''
from math import floor
def roundPricesToMatchTarget(prices, target):
    floor_array = map(lambda x : floor(x),prices)
    delta = int(round(target - sum(floor_array)))
    sorted_prices = sorted(enumerate(prices), key=lambda x: x[1] - floor(x[1]))
    for _ in range(delta):
        floor_array[sorted_prices.pop()[0]] += 1
                      
    result = [int(i) for i in floor_array]
    return result