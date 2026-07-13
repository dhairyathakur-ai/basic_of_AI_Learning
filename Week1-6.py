try:
    a=10
    b=0
    res=a/b
    print(res)
except ZeroDivisionError:
    print("can't divide by zero")

def count_evens(x):
    nums=0
    for n in x:
        if n%2==0:
            nums=nums+1
    return nums
print(count_evens([1,2,3,4,5]))

def reverse_list(x):
    res=[]
    for n in x:
        res.insert(0,n)
    return res
print(reverse_list([1,2,3,4,5]))

def reverse(x):
    x.reverse()
    return x
print(reverse([1,2,3,4,5]))

x=[1,2,3]
x.insert(0,0)
print(x)

letters=["a","b","d","e"]
letters.insert(2,"c")
print(letters)

def build_reversed(x):
    res=[]
    for n in x:
        res.insert(0,n)
    return res
print(build_reversed([1,2,3,4,5]))

def safe_divide(a, b):
    try:
        return a/b
    except:
        return "ERROR"
print(safe_divide(10,2))
print(safe_divide(10,0))

# List Comprehension

numbers=[4,15,8,23,42,9]
res=[n for n in numbers if n>10]
print(res)

n=[1,2,3,4,5,6,7,8,9,10]
ress=[x*x for x in n if x%2!=0]
print(ress)

l=["a","b",'c','d']
resss=[a.upper() for a in l ]
print(resss)

words=["hello","BYe","hiii","asdfgh"]
result=[len(x) for x in words]
print(result)

res1=[x*2 for x in n if x%2==0]
print(res1)

