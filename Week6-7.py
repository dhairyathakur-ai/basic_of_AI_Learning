v = [1,2,3] # Vector



"""Why vectors and matrices matter for AI

A row of data (like "age, height, weight" for one person) = a vector
A whole dataset (many people, many columns) = a matrix
Neural networks are, underneath, just doing lots of math on vectors and matrices"""

num=[1,2,3,4]
mean = sum(num)/len(num)
print(mean)

def find_mean(x):
    mean=sum(x)/len(x)
    return mean
print(find_mean([1,2,3,4,5]))

def find_median(x):
    a=sorted(x)
    b=len(a)//2
    return a[b]
print(find_median([1,3,5,7]))

def find_range(x):
    range = max(x)-min(x)
    return range
print(find_range([1,2,3,4,5,6]))

def upgraded_median(x):
    a = sorted(x)
    b = len(a)
    mid=b//2
    if b%2==0:
        return (a[mid-1]+a[mid]) /2
    else:
        return a[mid]
print(upgraded_median([1,3,2,6,5,8]))

m= [
    [1,2,3], # Matrix
    [4,5,6]
]
print(m[0][2])

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
total = 0
for row in matrix:
    for value in row:
        total = total + value
print(total)

# Standard Daviation

import statistics
print(statistics.stdev([1,44,23,65]))
