import time

def fibo_gen(n_max):
    '''
    Generator that creates the Fibonacci Series
    '''
    n1 = 0
    n2 = 1
    counter = 0
    while counter < n_max:
        
        if counter == 0:
            counter += 1
            yield n1
        
        elif counter == 1:
            counter += 1
            yield n2

        else:
            n_aux = n1 + n2
            n1, n2 = n2, n_aux
            counter += 1
            yield n_aux

    



def my_gen():
    print('hello world')
    n = 0
    yield n

    print('Hello heaven')
    n = 1
    yield n

def run():
    a = my_gen()
    print(next(a))
    print(next(a))
    #print(next(a))
    print('\n')
    print('**************Printing Fibonacci with Generators')
    max_n = int(input('Input how many numbers do you want: '))
    fibo_numbers = fibo_gen(max_n)
    for number in fibo_numbers:
        print(number)
        #time.sleep(1)

if __name__=='__main__':
    run()