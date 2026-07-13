#Write a function called average_of_evens that takes a list of numbers, and returns the average of only the even numbers in it.
def average_of_evens(x):
    total=0
    count=0
    for i in x:
        if i%2==0:
            total =total+i
            count=count+1
    average = total/count
    return average
print(average_of_evens([1,2,3,4,5,6]))

#Write a function called row_totals that returns a list containing the sum of each row.

def row_total(m):
    result=[]
    for row in m:
        result.append(sum(row))
    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(row_total(matrix))

#Write a function called column_totals that returns the sum of each column instead of each row.

def column_total(m):
    result=[0,0,0]
    for row in m:
        for i in range(3):
            result[i]=result[i]+row[i]
    return result
print(column_total(matrix))

#Write a list comprehension that returns only the scores above the average.
scores = [55, 90, 42, 88, 67, 30, 95]
average=sum(scores)/len(scores)
res=[s for s in scores if s>average]
print(res)
print(average)

#Write a function called min_max that takes a list and returns both the smallest and biggest number, using Python's built-in min() and max().

def min_max(m):
    return min(m),max(m)
low, high=min_max([1,2,4,5,6,7,8])
print(low,high)