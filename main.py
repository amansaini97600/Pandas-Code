import pandas as pd
# data = {
#     "Name" : ["Amit", "rohit", "neha", "Pooja", "Karan", "Simran"],
#     "Age" : [18, 19, 18, 20, 19, 18],
#     "Marks" : [78, 85, 92, 67, 88, 95]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df["Name"])
# print(df["Name"][3])
# print(df["Marks"][3])

# df.head()
# df.tail()
# df.shape
# df.columns
# df.dtypes
# df.info()

# print(df.head())
# print(df.head(2))
# print(df.tail())
# print(df.tail(2))
# print(df.shape)
# print(df.columns)
# print("Name" in df.columns)
# print(df.dtypes)
# print(df.info())

# import pandas as pd

# data = {
#     "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
#     "Age": [18, 19, 18, 20, 19],
#     "Marks": [85, 72, 91, 88, 76]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.loc[2])
# print(df.loc[2, "Name"])
# print(df.iloc[2])
# print(df.iloc[2, 2])
# # print(df.iloc[2,"Name"]) # ye error dega kyunki string not  suported only integer
# print(df[["Name","Age"]])
# print(df.loc[3])
# print(df.iloc[4])
# print(df[df["Marks"]>80])
# # marksGto80 = df["Marks"]>80
# # print(df[marksGto80])
# print(df[df["Age"]==19])
# print(df[(df["Age"]==18) & (df["Marks"]>80)])

# import pandas as pd

# data = {
#     "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
#     "Age": [18, 19, 18, 20, 19],
#     "Marks": [85, 72, 91, 88, 76]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.sort_values("Marks"))
# print(df.sort_values("Marks", ascending=False))
# print(df["Age"].unique())
# print(df["Age"].nunique())
# print(df["Age"].value_counts())
# print(df.sort_values(["Age","Marks"],ascending=[True, False]))
# df["Result"] = "pass" if df["Marks"]>=50 else "Fails" # ye error dega kyunki pandas if else support nhi karta shayad
# df["Result"] = "fail"
# df.loc[df["Marks"]>=80, "Result"] = "Pass"
# df = df.rename(columns={"Name":"Student_Name"})
# df = df.rename(columns={"Name":"Student_Name","Marks":"Student_Marks"})
# df = df.drop("Age", axis = 1)
# df = df.drop(2, axis = 0)
# df = df.drop(2) # ye error dega kyunki exix required h
# df.insert(2, "City", ["Delhi", "Meerut", "Dehradun", "Haridwar", "Noida"])
# print(df)

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit", "Simran"],
    "Age": [18, 19, 18, 20, 19, 18],
    "Marks": [85, 72, 91, 88, 76, 95]
}

df = pd.DataFrame(data)

# print(df)
# print(df.shape)
# print(df["Age"].value_counts())
# print(df[df["Marks"]>80])
# print(df.loc[df["Marks"]>80, ["Name", "Marks"]]) # ye me kr ke dekh rha tha only two columns print
# print(df[(df["Age"]==18) & (df["Marks"]>80)])
# print(df.sort_values("Marks", ascending=False))

# df["Result"] = "Fail"
# df.loc[df["Marks"]>=80, "Result"] = "Pass"
# print(df)

# df = df.rename(columns={"Age":"Student_Age"})
# print(df)

# df = df.drop("Age", axis=1)
# print(df)

# Question 10 Final

# df = df.rename(columns={"Age":"Student_Age"}).sort_values("Marks", ascending=False)[df["Marks"]>=75].head(3)
# print(df)
#Mene ise ek hi line me kr diya  alag alag bhi kr sakta tha but sort me maja h

df = df(
    
)
