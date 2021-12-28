#Hola 3 -> Hola Hola Hola
#Input a number and make division by
from typing import Callable

def strings_multiplier(multip: int):
    """
    This closure returns a function that returns a string concatenated multiple times
    """
    def str_mult(my_string: str) -> str:
        assert type(my_string) == str , "You only can use strings"
        return multip * my_string
    return str_mult

def make_division_by(n: int) -> Callable[[int,int],float]:
    """
    This closure returns a function that returns the division of an x number by n
    """
    def number_func(x: int) -> float: 
        assert n != 0, "You can not divide by zero"
        return x / n
    return number_func


def run():
    #Test the multiplier
    multip3 = strings_multiplier(3)
    multip7 = strings_multiplier(7)
    print(multip3('Hola'))
    print(multip7('Juan'))
    #Test division by
    division_by2 = make_division_by(2)
    division_by13 = make_division_by(13)
    print(division_by2(50))
    print(division_by13(1516516515))
    division_by0 = make_division_by(0)
    print(division_by0(100))


if __name__=='__main__':
    run()