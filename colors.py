import colorgram

color_palette = []


def color_extractor(image):
    colors = colorgram.extract(image, 2 ** 10)
    for one_color in colors:
        rgb = one_color.rgb
        r = rgb.r
        g = rgb.g
        b = rgb.b
        color_tuple = (r, g, b)
        color_palette.append(color_tuple)
    return color_palette


color_extractor('image.jpg')
