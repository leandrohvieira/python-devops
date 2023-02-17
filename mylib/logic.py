import wikipedia


def wiki(name="war Goddess", lenght=1):
    my_wiki = wikipedia.summary(name, lenght)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for Names"""

    results = wikipedia.search(name)
    return results