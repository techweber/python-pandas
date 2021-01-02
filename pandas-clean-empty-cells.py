import pandas as pd

df = pd.read_csv('dirtydata.csv')

# removing empty cells
# new_df = df.dropna()
# print(new_df.to_string())

# fill empty cells
# df.fillna(130,inplace=True)
# print(df)

# replace empty cells in specified column
# df['Calories'].fillna(130,inplace=True)
# print(df)

# replace empty values using mean method
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace=True)
# print(x)

# replace empty values using median method
# x = df["Calories"].median()
# df["Calories"].fillna(x, inplace=True)
# print(df)


# replace empty values using mode method
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)
print(df)