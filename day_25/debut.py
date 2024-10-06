import csv
from pandas import * as pd


#with open("weather_data.csv") as file:
#    list = []
#    for data in file:
#        list.append(data)
#    print(list)

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        temperature.append(row[1])
    temperature.remove(temperature[0])
    #print(temperature)
    temp = []
    for i in temperature:
        temp.append(int(i))
        temperature = temp
    print(temperature)