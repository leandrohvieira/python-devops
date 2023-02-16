import wikipedia


def wiki(name="war Goddess", lenght=1):
    my_wiki = wikipedia.summary(name, lenght)
    return my_wiki
