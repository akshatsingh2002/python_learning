import pandas as pd
df = pd.read_csv("fortune_data.csv")
# print(df.info())
# print(df["Rank"].nunique())
# print(df.groupby("Rank").count()>1) learn dupblicate
df.set_index("Rank",inplace=True)
print(df)
df.reset_index(drop=True, inplace=True)
print(df)
