import pandas as pd


xlsx = pd.ExcelFile("D:\Rehpy")
df = pd.read_excel(xlsx, 'Sheet1')



df.head()


