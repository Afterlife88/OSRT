from __future__ import division
from decimal import Decimal

# Series module

def sumOfSeries(n):
    sum = Decimal(0.0)
    for i in range(1, n+1):
        sum += Decimal(pow(i / (i + 1), pow(i, 2)))
    return Decimal(sum)
