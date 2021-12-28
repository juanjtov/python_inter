from datetime import datetime

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        #Here you execute the function to be decorated
        func(*args,**kwargs)
        #Finish the decoration
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'It took {time_elapsed.total_seconds()} seconds')
    return wrapper

@execution_time
def random_func():
    print('Execution time for a for loop a lot of times')
    for _ in range(1,100000000):
        pass

@execution_time
def addition(a:int, b:int) -> int:
    return a + b 

#The argument of this function is a keyword argument because its nameable
@execution_time
def say_hi(name='Juan Jose'):
    print(f'Hi {name} ')

if __name__=='__main__':
    random_func()
    print('Addition function')
    addition(5,1516516156)
    say_hi('Facundo')