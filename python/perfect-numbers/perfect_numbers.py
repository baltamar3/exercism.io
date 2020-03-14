def classify(number):
    if number <= 0: raise ValueError("El número debe ser positivo")

    res = sum(i for i in range(1,number) if number % i == 0) 
    if res > number: return "abundant"
    elif res < number: return "deficient"
    else: return "perfect"
