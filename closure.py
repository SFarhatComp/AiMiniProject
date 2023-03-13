

def general(some_algo, some_arg: str)->None:
    print('we are going to execute some random code passed to us')
    some_algo(some_arg)
    print('bye')



def algo1(x):
    print(f'hello {x}')

def algo2(x):
    print(f'nik ta mere {x}')


general(algo1, 'sami')
general(algo2, 'hicham')