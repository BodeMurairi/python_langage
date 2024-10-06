import pandas as pd

# Data file extracted
data = pd.read_csv("central_park.csv")
red_colour = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_colour = len(data[data["Primary Fur Color"] == "Gray"])
black_colour = len(data[data["Primary Fur Color"] == "Black"])

colours_dict = {"Fur Color":["Gray", "Red", "Black"],
                "Count":[gray_colour, red_colour, black_colour]}
new_colours_dict = pd.DataFrame(colours_dict)
print(new_colours_dict)
new_colours_dict.to_csv("First_data.csv")