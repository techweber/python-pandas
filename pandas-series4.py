import pandas as pd

data = {
	"calories": [420,380,390],
	"duration": [50,40,45],
	"food": ["apple","banana","cherry"]
}
myvar = pd.DataFrame(data)
print(myvar)
