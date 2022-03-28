def color_code(color: str):
    """
    The function return the real value of resistor based on passed parameter color
    :param color: string -> nome de uma cor
    :return: int -> retorna o index da cor obtida como parâmetro
    """
    return colors().index(color)


def colors():
    """
    The functions return a list colors to be used in the marking of resistor values
    :return: list -> lista de cores
    """
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
