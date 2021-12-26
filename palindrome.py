
def is_palindrome(string: str) -> bool:
    #Ana is not hte same than ana
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def is_prime(num):
    count = 0

def run():
    print(is_palindrome(1000))


if __name__== '__main__':
    run()