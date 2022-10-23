import sqlite3
import controller
import view

bd = sqlite3.connect("Data_base.db")
cursor = bd.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
)''')

#baza = [(1,'Ivan','Ivanov','head ingenier',50000,10000),
        #(2,'Igor','Semenov','ingenier',20000,8000),
        #(3,'Oleg','Petrov','zavhoz',12000,3000)]

#try:
    #cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)',baza)
    #bd.commit()
#except:
    #print('Data is exist')
#for i in cursor.execute('SELECT * FROM personal'):
    #print(*i)

#cursor.execute('SELECT * from personal WHERE name LIKE "Oleg";')
#one = cursor.fetchmany()
#print(*one)
#cursor.execute('SELECT * from personal WHERE id=2;')
#one = cursor.fetchone()
#print(*one)

#cursor.execute("DELETE FROM users WHERE lname='Parker';") example of deleting
#bd.commit()

def preview_base():
    list_dt = []
    for i in cursor.execute('SELECT * FROM personal'):
        list_dt.append(i)
    return list_dt

def add_record():
    data = controller.info_for_record()
    cursor.execute('INSERT INTO personal VALUES(NULL,?,?,?,?,?)', data)
    bd.commit()

def delete_record(id):
    try:
         cursor.execute(f'DELETE from personal WHERE id={id}')
         bd.commit()
         return 'запись удалена'
    except:
        return 'записи с таким id нет'

def find_record():
    section, meaning = controller.info_for_search() #тут из функции получаем кортеж, и присваиваем переменным значения
    query = f"SELECT * FROM personal WHERE {section} LIKE '{meaning}'"
    list_dt=[]
    for i in cursor.execute(query):
        list_dt.append(i)
    return list_dt

def update_record():
    section, id, new_value = controller.info_for_update()
    if section in ('salary','bonus'):
        new_value = int(new_value)
    query = f"UPDATE personal SET {section} = '{new_value}' WHERE id={id}"
    cursor.execute(query)
    bd.commit()
    return 'запись обновлена'

def selective_view():
    columns, condition = controller.info_for_select()
    query = f"SELECT {columns} FROM personal {condition}"
    print(query)
    list_dt = []
    for i in cursor.execute(query):
        list_dt.append(i)
    return list_dt



#cursor.execute('UPDATE personal SET salary = 55000 WHERE id=2')
