import re
alfabeto = "abcdefghijklmnopqrstuvwxyz"
def is_pangram(sentence):
    sentence = re.findall ("[a-z]", sentence.lower())
    for i in alfabeto:
        if i not in sentence:
            return False
    return True
