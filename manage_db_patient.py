import sqlite3

conp = sqlite3.connect("userdatapatient.db", check_same_thread=False)
cp = conp.cursor()


def create_patient_table():
    cp.execute('CREATE TABLE IF NOT EXISTS patient_table(username TEXT, password TEXT)')


def add_patient_data(username, password):
    cp.execute('INSERT INTO patient_table(username,password) VALUES (?,?)', (username, password))
    conp.commit()


def login_patient(username, password):
    cp.execute('SELECT * FROM patient_table WHERE username =? AND password = ?', (username, password))
    data = cp.fetchall()
    return data


def view_all_patient():
    cp.execute('SELECT * FROM patient_table')
    data = cp.fetchall()
    return data
