# import pandas as pd
# import openpyxl
# workbook = openpyxl.load_workbook("Book1.xlsx")
# df = pd.read_excel('Book1.xlsx')

# # print(df)

# # import openpyxl
# # from openpyxl import Workbook
# # path="Book1.xlsx"
# # wb_obj = openpyxl.load_workbook(path)
# # sheet_obj = wb_obj.active
# # row = sheet_obj.max_row
# # column = sheet_obj.max_column
# # print(row,column)
# # for i in range(1,row+1):
# #     cell_obj = sheet_obj.cell(row = i , column = 1)
# #     print(cell_obj.value) 
    
# # for i in range(2,row+1):
# #     cell_obj = sheet_obj.cell(row = i , column = 2)
# #     cell_obj.value = "yes" 
    
# # wb_obj.save("Book1.xlsx")


import pandas as pd 
df = pd.DataFrame({1:[1,2,3],2:[3,4,5]})
print(df)
df.to_excel("pandas.xlsx")
df2 = pd.read_excel("pandas.xlsx")
print(df2)