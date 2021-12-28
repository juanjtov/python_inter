'''
Avoid this kind of things, if you reverse the order of how you call the functions
you might have big issues
'''
fruit = ['pineapple', 'grapes', 'apple', 'banana']

def first_item():
    global fruit
    fruit = fruit[0]
    
def iterate():
    global fruit
    for entry in fruit:
        print(entry)
    


x = 20

def my_func():
    #if you want to modify and use the global var use the global keyword
    global x
    x = x +1
    print(x)

def my_other_func():
    
    x = 8
    print(x)


z = 5

def func1():
    z = 3

    def func2():
        z = 2
        print(z)

    func2()
    print(z)
    

if __name__=='__main__':
    # iterate()
    # print(fruit)
    # first_item()
    # print(fruit)
    #my_func()
    #my_other_func
    func1()
    print(z)