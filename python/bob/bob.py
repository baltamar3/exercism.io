def response(hey_bob):
    if hey_bob.strip and (hey_bob=="" or hey_bob.isspace()) : return "Fine. Be that way!"
    elif hey_bob.rstrip().endswith("?") and hey_bob.isupper() : return "Calm down, I know what I'm doing!"
    elif hey_bob.rstrip().endswith("?") : return "Sure."
    elif hey_bob.isupper() : return "Whoa, chill out!"
    else: return "Whatever."
