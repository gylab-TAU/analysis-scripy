def get_coordinates(x, y, width, height):
    left = x
    right = x + width
    top = y
    bottom = y + height

    return {
        "left": left,
        "right": right,
        "top": top,
        "bottom": bottom
    }

def getOverlappefArea(x1, y1, width1, height1, x2, y2, width2, height2):
    pic1 = get_coordinates(x1, y1, width1, height1)
    pic2 = get_coordinates(x2, y2, width2, height2)

    x_overlap = max(0, min(pic1["right"], pic2["right"]) - max(pic1["left"], pic2["left"]))
    y_overlap = max(0, min(pic1["bottom"], pic2["bottom"]) - max(pic1["top"], pic2["top"]))

    return x_overlap * y_overlap


