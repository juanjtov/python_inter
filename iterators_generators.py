import time


def iterator(my_list):
    """For loop inside, transform an iterable to an iterator object and
        iterate over each element"""
    while True:

        try:
            element = next(my_iter)
            print(element)

        except StopIteration:
            break


class EvenNumbers:
    """Class which implements an iterator of all even number, o
        or even numbers until max"""

    def __init__(self,max=None):
        self.max = max

    def __iter__(self):
        #Define first even number and return the object
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result

        else:
            raise StopIteration



class FiboIter:
    '''
    Class that defines an iterator for the Fibonacci succession
    '''
    def __init__(self, n = None):
        self.max = n

    def __iter__(self):
        #Define the first two numbers of the fibonacci succession
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        #If the iter didn't received a max number or the counter is less than that number
        if not self.max or self.counter < self.max:

            if self.counter == 0:  
                self.counter += 1
                return self.n1

            elif self.counter == 1:
                self.counter += 1
                return self.n2

            else:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                #**********Using the Python swaping concept *********************
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1

                return self.aux

        else:
            raise StopIteration

if __name__=='__main__':
    #Simple Examples
    my_list = [1,2,3,4,5]
    my_iter = iter(my_list)
    #Building iterators *********Printing N numbers of the Fibonacci Sequence ********
    print('**********Printing N numbers of the Fibonacci Sequence*********')
    print('\n')
    numbers = int(input('Introduce the amount of numbers you would like to know: '))
    fibonacci = FiboIter(numbers)
    for element in fibonacci:
        print(element, end=" ")

    # fibonacci = FiboIter()
    # for element in fibonacci:
    #     print(element)
    #     #Pause 01 sec after each printin
    #     time.sleep(1)