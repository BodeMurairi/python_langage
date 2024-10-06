import colorgram

color_extract = colorgram.extract("/home/bode/Documents/programming/100_days_ofCode/day_18/my_venv/hirst_painting/image.webp", 30)
#print(color_extract)

# getting a list of different colors
color = []

for i in color_extract:
    r = i.rgb.r 
    g = i.rgb.g 
    b = i.rgb.b
    rgb_color = (r, g, b)
    color.append(rgb_color)



new_color = [(207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 207, 104), (132, 177, 203), (158, 46, 83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69), (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), (88, 157, 92), (78, 153, 164), (195, 78, 72), (45, 74, 78), (80, 74, 44), (162, 201, 218), (58, 126, 122), (218, 176, 187), (169, 207, 170), (220, 181, 168)]