import pandas as pd
df = pd.read_csv("NbaInfo.csv")
df.dropna(how="any",inplace=True)
# print(df)
# print(df.info())
# df["Name"] = df["Name"].astype("category")
# df["Salary"].fillna(0,inplace=True)
# df["Age"].fillna(0,inplace=True)
# df["Number"].fillna(0,inplace=True)
# df["Salary"]= df["Salary"].astype(int)
# df["Age"]= df["Age"].astype(int)
# df["Number"]= df["Number"].astype(int)
# print(df.info())


# print(df[df["Position"]=="PG"])
# print(df[(df["Position"]=="PG")].count())


print(df.groupby("Position").count())
print(df.groupby("Position").first())