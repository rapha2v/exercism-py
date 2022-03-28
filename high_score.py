def latest(scores: list):
    """
    The function returns the last score obtained
    :param scores: list -> lista de pontuações
    :return: int -> Retorna a última pontuação obtida
    """
    return scores[-1]


def personal_best(scores: list):
    """
    The function returns the best score obtained
    :param scores: list -> lista de pontuações
    :return: int -> Retorna a maior pontuação obtida
    """
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    """
    The function return the three best scores
    :param scores: list -> Lista de pontuações 
    :return: list -> Retorna as três melhores pontuações
    """
    scores.sort(reverse=True)
    return scores[:len(scores) - len(scores) + 3]
