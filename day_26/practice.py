import pandas as pd
import random

other_name = {"student":["Alex", "Alberto", "Ronald", "Jean-Felix"],
              "score": [50,60,25,75]
}
for (key, value) in other_name.items():
    print(value)

dataframe = pd.DataFrame(other_name)
print(dataframe)
for (key, value) in dataframe.items():
    print(key)

for (index, row) in dataframe.iterrows():
    print(row.score)
