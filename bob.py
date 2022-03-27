def response(hey_bob):
    """
    :param hey_bob: -> check if the phrase is a question, yell, yell question, nothing, or only talk to him
    :return:
    """
    if hey_bob.isupper() and not hey_bob.endswith('?'):
        return "Whoa, chill out!"
    elif hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.strip().endswith('?'):
        return "Sure."
    elif hey_bob.strip() == '':
        return "Fine. Be that way!"
    else:
        return "Whatever."


print(response("WATCH'S GOING ON?"))
