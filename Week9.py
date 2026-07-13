import numpy as np
import pandas as pd
arr = np.array([1,2,3,4,5])
print(arr)
print(arr+10)
print(arr*2)

arr1=np.array([10,20,30,40])
print(arr1*3)

ar=np.array([4,8,15,16,23,42])
print(ar.sum())
print(ar.mean())
print(ar.max())
print(ar.min())

new = np.array([5,10,15,20,25])
print(new.mean())
print(new.sum())

matrix =np.array([
    [1,2,3],
    [4,5,6]
])
print(matrix)
print(matrix.shape)

M=np.array([
    [1,2],
    [3,4],
    [5,6]
])
print(M.shape)

data ={
    "name": ["alex", "Sam", "Jordan"],
    "age" : [25,23,29]
}
df = pd.DataFrame(data)
print(df) # All Dataframe
print(df["age"]) # Accessing a coloumn
print(df.loc[2]) # Accessing a row

data1={
    "city": ["Delhi","Mumbai","chennai"],
    "population": [312900000,207033300,234400000]
}
df=pd.DataFrame(data1)
print(df)
print(df["population"])
print(df[df["population"] > 250000000])


"""Question 1: Array math
Create a NumPy array [2, 4, 6, 8, 10]. Print the array after subt
jracting 1 from every number."""
Arr=np.array([2,4,6,8,10])
print(Arr-1)

# Question 2: Find above-average values
"""Create an array [10, 25, 30, 5, 40, 15].
Use .mean() to find the average, then print only the
values greater than the average """
mean_arr=np.array([10,25,30,5,40,15])
average=mean_arr.mean()
print(average)
print(mean_arr[mean_arr>=average])

# Question 3: 2D array shape
# Create a 2D NumPy array with 4 rows and 2 columns (make up any numbers). Print its .shape and confirm it shows (4, 2).

matrices=np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
print(matrices.shape)

"""Add a new column called "passed" that is True if score is 60 or above, False otherwise"""

data={
    "name": ["Alex","Sam","Jordan"],
    "Score":[85,60,92]
}
df=pd.DataFrame(data)
df["passed"]=df["Score"]>=80
print(df)

"""Question 5: Sort a DataFrame
Using the same df, sort it by "score" from highest to lowest."""
df_sorted=df.sort_values("Score", ascending=False)
print(df_sorted)

"""Question 6: Basic stats on a column
Using the same df, print the average score using .mean() on the "score" column."""
print(df["Score"].mean())

#Handling Missing Data


Data={
    "Name":["Alex","Jordan","Sam"],
    "Score":[85,np.nan,92]
}
df=pd.DataFrame(Data)
print(df)
print(df.isna())
df.Score=df.Score.fillna(df.Score.mean())
print(df)

df_clean=df.dropna()
print(df)

DAta={
    "team":["A","A","B","B"],
    "score":[10,20,30,40]
}
df=pd.DataFrame(DAta)
print(df.groupby("team")["score"].prod())

data = {
    "student": ["A", "B", "C", "D"],
    "class": ["Math", "Math", "Science", "Science"],
    "marks": [70, 90, 60, 80]
}
df = pd.DataFrame(data)
print(df.groupby("class")["marks"].mean())

