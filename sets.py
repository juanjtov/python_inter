
def remove_duplicates(some_list: list) -> list:
    '''
    Remove duplicates using brute force
    '''
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def remove_duplicates_sets(some_list: list) -> set:
    '''
    Remove duplicates using sets
    '''
    return list(set(some_list))

def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))
    print('\n')
    print('*********Now using sets*******')
    print('\n')
    print(remove_duplicates_sets(random_list))

if __name__=='__main__':
    run()