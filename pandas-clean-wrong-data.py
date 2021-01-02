import pandas as pd
df = pd.read_csv('dirtydata.csv')
print(df.duplicated())
# for x in df.index:
# 	if df.loc[x,"Duration"] > 120:
# 		df.drop(x, inplace=True)
# df['Date'] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'],inplace=True)
# df.index(7)["Duration"] = 45
# print(df.to_string())