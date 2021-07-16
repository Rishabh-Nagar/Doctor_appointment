import sqlite3

cur_d = sqlite3.connect("current_data_doctor.db", check_same_thread=False)
cud = cur_d.cursor()


def create_current_doctor_table():
    cud.execute('CREATE TABLE IF NOT EXISTS current_doctor_table(name TEXT, age INTEGER, sex TEXT, degree TEXT, cur_hosp TEXT)')


def add_current_doctor_data(name, age, sex, degree, cur_hosp):
    cud.execute('INSERT INTO current_doctor_table(name, age, sex, degree, cur_hosp) VALUES (?,?,?,?,?)', (name, age, sex, degree, cur_hosp))
    cur_d.commit()


def view_all_current_doctor():
    cud.execute('SELECT * FROM doctor_table')
    data = cud.fetchall()
    return data
