import model as md
import view

def input_choice():
    while True:
        user_choice = input('1 - просмотреть всю базу, '
                            '2 - добавить запись, '
                            '3 - удалить запись, '
                            '4 - найти запись '
                            '5 - редактировать запись '
                            '6 - получить свод данных '
                            'q - ВЫХОД'
                            ': ')
        if user_choice == '1':
            data = md.preview_base()
            view.print_data(data)
        elif user_choice == '2':
            md.add_record()
        elif user_choice == '3':
            data = view.get_info('Введите id')
            result = md.delete_record(data)
            view.print_result(result)
        elif user_choice == '4':
            data = md.find_record()
            view.print_data(data)
        elif user_choice == '5':
            result = md.update_record()
            view.print_result(result)
        elif user_choice == '6':
            data = md.selective_view()
            view.print_data(data)
        elif user_choice == 'q':
            print('Exit')
            break

def info_for_record():
    info = []
    for i in ['Имя','Фамилия','Должность','Оклад','Премия']:
        answer = view.get_info(i)
        if answer.isdigit():
            info.append(int(answer))
        else:
            info.append(answer)
    return tuple(info)

def info_for_search():
    info = []
    dict_columns = {'1':'name',
          '2': 'last_name',
          '3':'position',
          '4':'salary',
          '5':'bonus'
            }
    for i in dict_columns:
        print(i,' - ',dict_columns[i])
    info.append(dict_columns[view.get_info('Укажите номер столбца, по которому искать')])
    info.append(view.get_info('Укажите значение по которому искать'))
    return tuple(info)

def info_for_update():
    info = []
    dict_columns = {'1': 'name',
                    '2': 'last_name',
                    '3': 'position',
                    '4': 'salary',
                    '5': 'bonus'
                    }
    for i in dict_columns:
        print(i, ' - ', dict_columns[i])
    info.append(dict_columns[view.get_info('Укажите номер столбца,  в котором заменить значение')])
    info.append(int(view.get_info('Укажите id')))
    info.append(view.get_info('Укажите новое значение'))
    return tuple(info)

def info_for_select():
    res_data_list=[]
    dict_columns = {'1': 'name',
                    '2': 'last_name',
                    '3': 'position',
                    '4': 'salary',
                    '5': 'bonus'
                    }
    for i in dict_columns:
        print(i, ' - ', dict_columns[i])
    columns_list = view.get_info('Укажите через запятую номера столбцов, которые нужно вывести').split(',')
    for i in range(0,len(columns_list)):
        columns_list[i] = dict_columns[columns_list[i]]
    res_str=','.join(columns_list)
    res_data_list.append(res_str)
    answer = view.get_info('Фильтровать? (да / нет)')
    if answer == 'да':
        filter_colmn = 'WHERE ' + dict_columns[view.get_info('Укажите номер столбца, по которому сортировать')]
        filter_colmn += view.get_info('Укажите условие (=,>,<,>=,<=) и значение')
        res_data_list.append(filter_colmn)
    else:
        filter_colmn = ''
        res_data_list.append(filter_colmn)
    return tuple(res_data_list)