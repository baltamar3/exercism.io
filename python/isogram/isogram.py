def is_isogram(string):
    new_str = join_str(string)
    for letter in new_str:
        if new_str.count(letter) > 1: return False
    return True

def join_str(string):
    new_str = ""
    if "-" in string: new_str=string.split("-")
    else: new_str=string.split(" ")
    new_str = "".join(new_str).lower()
    return new_str