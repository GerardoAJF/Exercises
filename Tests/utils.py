def color_print(color: str, text) -> str:
    color = color.lstrip("#")

    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)

    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

