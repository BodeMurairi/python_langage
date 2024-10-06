import pandas as pd

data = pd.read_csv("weather_data.csv")
#print(type(data))
data_temp = data["temp"] # data serie
monday= data[data.day == "Monday"]
monday_temp = monday.temp[0]
temp_fr = (monday_temp * 9/5)+32
print(f"temperature for Monday in Fr is :{temp_fr}")


