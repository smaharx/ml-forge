import numpy as np
import pandas as pd


print("Lab 1 ML")




# print("Day1 ")


# print('basic arthmetic operations and operators')

# a, b = 17, 5
# print(a / b, a % b, a ^ 2) 


# name, age = "Ali", 21
# gpa = float("3.85")
# print(type(name), type(age), type(gpa))



# a, b = 17, 5
# print(a // b, a % b, a**2)  
# print(3 in [1, 2, 3])  
# print(5 & 1, 5 | 2, 5 ^ 1, ~5)  

# for i in range(0, 10):
#     if i == 4:
#         continue
#     print(i, end=" ")
# print()

# x = 10
# print("even" if x % 2 == 0 else "odd")

 



# print("Day2")
# print('methods and concepts based on arguements and method call with parameters ')


# def intro(name, msg="Hello"):
#     return f"{msg}, {name}!"


# def total(*num):
#     return sum(num)


# def show(**kwargs):
#     return kwargs

# square = lambda x: x**2
# print(intro("Mubashir",'matric' ), total(7, 2, 3,9,1), show(a=4, b='ahmed'), square(6))




# print("\nList ---")
# lst = [1, 2, 3, 4, 5]
# print(lst[1:3], lst[::-2])



# print('Numpy start')

# arr = np.array([[1, 2, 3,33,34,57], [4, 5, 6,49,50,67]])
# print(arr.shape, arr.ndim, arr.size, arr.dtype)
# print()


# m = np.arange(1, 21).reshape(4   , 5)

# print(m.sum(axis=0), m.sum(axis=1), m.mean(), m.std())
# print(m[m > 15])
# print(np.where(m % 2 == 0, 1, 0))





print('\n\n pandas : ')



data = {"name": ["Ali", "Sara", "Omar",'Ahmed','me'], "marks": [78, 92, 65,96,40]}
df = pd.DataFrame(data)
print(df.head())
print(df.describe())
print(df.info())

top = df[df["marks"] > 70]
print(top.sort_values("marks", ascending=True))
print(df.loc[0, "name"], df.iloc[0, 1])




students = pd.DataFrame(
    {
        "name": ["A", "B", "C", "D", "E", "F"],
        "subject": ["Math", "CS", "Math", "CS", "Math", "CS"],
        "marks": [88, 45, 76, 92, 60, 81],
    }
)
print(students.shape, students.columns.tolist())
print(students.info(), students.describe())
print(students[students["marks"] > 80])

# print(students.loc[2, "name"], students.iloc[2, 0])  