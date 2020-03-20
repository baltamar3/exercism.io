def find_anagrams(word, candidates):
    word_s = sorted(word.lower())
    lista=[]
    for candidate in candidates:
        aux = sorted(candidate.lower())
        if aux == word_s:
            if candidate.lower() != word.lower():
                lista.append(candidate)
    return lista
        
