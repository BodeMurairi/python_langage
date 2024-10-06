import pandas as pd

#open data
data = pd.read_csv("central_park.csv")

# colour types: Gray, Red, Black
# Select fur colour column
primary_colour = data["Primary Fur Color"]
primary_colour.to_list()

red_type = []
gray_type = []
black_type = []
for colours in primary_colour:
    if colours == "Cinnamon":
        red_type.append(colours)
    elif colours == "Black":
        black_type.append(colours)
    elif colours == "Gray":
        gray_type.append(colours)

colour_fur = {"Fur Color": ["gray", "red", "black"],
              "Count": [len(gray_type), len(red_type), len(black_type)]}
colour_fur = pd.DataFrame(colour_fur)
colour_fur.to_csv("analysis_2.csv")
print(colour_fur)