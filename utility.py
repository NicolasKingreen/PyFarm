def change_color(color, shift=1):
    new_color = list(color)
    if shift == 0:
        pass
    elif shift == 1:
        new_color[0], new_color[1], new_color[2] = new_color[1], new_color[2], new_color[0]
    elif shift == 2:
        new_color[0], new_color[1], new_color[2] = new_color[2], new_color[0], new_color[1]
    return tuple(new_color)
