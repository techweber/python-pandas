import pandas as pd
calories = {"day1":420,"day2":380,"day3":390}
myvar = pd.Series(calories, index=["day3","day2"])
print(myvar)
