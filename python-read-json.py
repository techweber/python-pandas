# import pandas as pd
# df = pd.read_json('data.json')

# print(df.to_string())

# # print(df)


import pandas as pd
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  }
}

df = pd.DataFrame(data)

print(df)
