import sqlite3

def init_db():
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hospital (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fio TEXT UNIQUE NOT NULL,
               diagnosis TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()


def InsertUser(fio, diagnosis):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute ('''INSERT INTO hospital (fio, diagnosis) 
                        VALUES (?,?)''',(fio, diagnosis))

        conn.commit()
        conn.close()

def update_user(id, fio, diagnosis):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE hospital SET fio = ?, diagnosis = ?
        WHERE id = ?
    ''', (fio, diagnosis, id))
    conn.commit()
    conn.close() 
        
def delete_user(id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor() 
    cursor.execute('DELETE FROM hospital WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def get_user_by_id(id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hospital WHERE id = ?', (id,))
    user = cursor.fetchone()  
    conn.close()
    return user

if __name__ == '__main__':
    init_db()

    #id = int(input("Введите id для обновления: "))
    #fio = input("Введите новое ФИО: ")
    #diagnosis = input("Введите новую должность: ")
    #update_user(id, fio, diagnosis)

    #id = int(input("Введите id для удаления: "))
    #delete_user(id) 

    #fio=input("Введите ФИО: ")
    #diagnosis=input("Введите диагноз: ")
   # InsertUser(fio, diagnosis)

    #user_data = get_user_by_id(id)  
    #if user_data:
    #    print("Данные пользователя:")
    #    print(f"ID: {user_data[0]}")
    #    print(f"ФИО: {user_data[1]}")
    #    print(f"диагноз: {user_data[2]}")
    #else:
    #    print(f"Пользователь с id {id} не найден.")
