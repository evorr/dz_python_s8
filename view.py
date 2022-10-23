
def get_info(param):
    return input(f'{param}: ')

def print_data(data): #сюда приходит список с кортежами
    for i in data:
        for val in i:
            print(val,' ', end='')
        print('')

def print_result(result):
    print(result)