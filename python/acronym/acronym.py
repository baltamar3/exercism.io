import re
def abbreviate(words):
    words = re.findall(r"['A-Za-z]+", words)
    aux=""
    for word in words: 
        aux+=word[0]
    return aux.upper()
