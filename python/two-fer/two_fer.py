def two_fer(name : str = "you") -> str:
    """
    Given a name, return a string with the message "One for name, one for me."

    :param name: str - name to put at the message. If name is missing, we put "you".
    :return: str - the personalized message.
    """

    return f"One for {name}, one for me."
