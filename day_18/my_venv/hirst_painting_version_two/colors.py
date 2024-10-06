import colorgram

# extract colours
extract_colors = colorgram.extract("/home/bode/Documents/programming/100_days_ofCode/day_18/my_venv/hirst_painting_version_two/image.webp", 60)

# getting rgb colors
rgb_colours = []

for i in extract_colors:
    r = i.rgb.r 
    g = i.rgb.g 
    b = i.rgb.b
    
    colors = (r, g, b)
    rgb_colours.append(colors)

print(rgb_colours)
