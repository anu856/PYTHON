
import pandas as pd
df=pd.read_csv("MonthlyProductSales.csv",encoding="ISO-8859-1")
print(df)
print(df.head(n=10))
df.tail(n=10)