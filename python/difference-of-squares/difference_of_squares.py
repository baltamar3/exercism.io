def square_of_sum(number):
    """Sumo los números y luego obtengo el cuadrado de la suma"""
    return pow( sum([i for i in range(number+1)]), 2 )


def sum_of_squares(number):
    """Obtengo los cuadrados de los números y luego sumo"""
    return sum( [pow(i,2) for i in range(number+1)] )


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
