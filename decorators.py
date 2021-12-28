from typing import Callable

def mayus(func: Callable) -> Callable:
    def wrapper(text: str):
        return func(text).upper()
    return wrapper

@mayus
def message(name: str) -> str:
    return f'{name} you received a message'

def run():
    print(message('Juan Jose'))

if __name__=='__main__':
    run()