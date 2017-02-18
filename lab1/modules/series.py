from __future__ import division

# Series module

def sumOfSeries(n):
    sum = 0.0
    for i in range(1, n+1):
        sum += pow(i / (i + 1), pow(i, 2))
    return sum
