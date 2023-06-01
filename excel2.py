import pandas as pd 
# import openpyxl
# from openpyxl.workbook import Workbook
# df = pd.DataFrame({1:[1,2,3],2:[3,4,5]})
# df.columns = ["name","number"]
# df.index = [1,2,3]
# print(df)
# df.to_excel("pandas.xlsx")

df = pd.DataFrame({1:[1,2,3],2:[4,5,6]})
df2 =pd.DataFrame({1:[10,20],2:[40,]},ignore_index=True)
dewdf = df._append(df2,ignore_index=True)
print(dewdf)

# import pandas as pd

# data1 = {
#   "age": [16, 14, 10],
#   "qualified": [True, True, True]
# }
# df1 = pd.DataFrame(data1)

# data2 = {
#   "age": [55],
#   "qualified": [True]
# }
# df2 = pd.DataFrame(data2)

# newdf = df1._append(df2,ignore_index=True)
# print(newdf)