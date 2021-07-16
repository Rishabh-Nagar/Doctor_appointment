import sqlite3

cond = sqlite3.connect("userdatadoctor.db", check_same_thread=False)
cd = cond.cursor()


def create_doctor_table():
    cd.execute('CREATE TABLE IF NOT EXISTS doctor_table(username TEXT, password TEXT)')


def add_doctor_data(username, password):
    cd.execute('INSERT INTO doctor_table(username,password) VALUES (?,?)', (username, password))
    cond.commit()


def login_doctor(username, password):
    cd.execute('SELECT * FROM doctor_table WHERE username =? AND password = ?', (username, password))
    data = cd.fetchall()
    return data


def view_all_doctor():
    cd.execute('SELECT * FROM doctor_table')
    data = cd.fetchall()
    return data
