from PIL import Image
import colorsys
import collections

color_families = {
    "red": (0, 0.05),
    "orange": (0.05, 0.11),
    "yellow": (0.11, 0.2),
    "green": (0.2, 0.4),
    "cyan": (0.4, 0.55),
    "blue": (0.55, 0.7),
    "purple": (0.7, 0.9),
    "pink": (0.9, 1.0)
    }
def group_hsv_to_color_families(hsv_list, color_families):
    color_dict = {key: [] for key in color_families.keys()}
    for hsv in hsv_list:
        for color, (min_hue, max_hue) in color_families.items():
            if hsv[0] >= min_hue and hsv[0] < max_hue:
                color_dict[color].append(hsv)
    return color_dict

def sort_hsv_by_brightness(hsv_list):
    return sorted(hsv_list, key=lambda hsv: colorsys.rgb_to_hsv(*colorsys.hsv_to_rgb(*hsv))[2])




def get_image_colors(image_path):
    # Open image and convert to RGB format
    with Image.open(image_path).convert('RGB') as image:
        colors = list(set(image.getdata()))

        #Sortiert die Farben in RGB, und entfernt Farblos, Weiß und Schwarz
        colors=sorted(colors)
        if (colors[0]==(0,0,0)):
            colors.remove(colors[0])
        if (colors[-1]==(255,255,255)):
            colors.remove(colors[-1])

        #Macht die RGB Werte in HSV Werte, sortiert sie nach Farbgruppen und macht ein Dictionary draus, und sortiert die Items in den Gruppen nach dem 'Value'
        hsv_colors = []
        for rgb in colors:
            hsv = colorsys.rgb_to_hsv(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)
            hsv_colors.append(hsv)        
        hsv_colors = sorted(hsv_colors, key=lambda x: x[0])
        dictionary=group_hsv_to_color_families(hsv_list=hsv_colors, color_families=color_families)

        dictionary = {k: sorted(v, key=lambda x: x[2]) for k, v in dictionary.items()}
        #print(dictionary)

        #Macht die Werte für Photshop zur Überprüfung aufmachbar
        sortedtransformed= collections.OrderedDict()
        for k, v in sorted(dictionary.items(), key=lambda x: x[1], reverse=True):
            # refactor the HSV values to degrees, percentages, etc.
            sorted_values = [(round(h * 360), round(s * 100), round(v * 100)) for (h, s, v) in sorted(v, key=lambda x: x[2])]
            # add the sorted and refactored values to the sorted_dict
            sortedtransformed[k] = sorted_values

        print(sortedtransformed)




        # Convert the unique HSV colors back to RGB and return as a list of tuples
        #print (colors)
        #print(rgb_list)


get_image_colors("./testmon/testmon/9.png")