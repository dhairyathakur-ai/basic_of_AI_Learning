import matplotlib.pyplot as plt
import pandas as pd
scores= [70,90,60,80]
students=["A","B","C","D"]
plt.bar(students, scores)
plt.show()

data = {
    "student": ["A", "B", "C", "D"],
    "marks": [70, 90, 60, 80]
}
df = pd.DataFrame(data)

df.plot(kind="pie", x="student", y="marks")
plt.title("Marks by Student")
plt.show()

data = {
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "sales": [100, 150, 130, 200]
}
df = pd.DataFrame(data)
df.plot(kind="bar",x="month",y="sales")
plt.title("Monthly Sales")
plt.show()