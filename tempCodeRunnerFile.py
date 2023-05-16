import pandas as pd
import openpyxl
workbook = openpyxl.load_workbook("Book1.xlsx")
df = pd.read_excel('Book1.xlsx')

print(df)