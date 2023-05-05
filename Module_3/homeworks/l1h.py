import os
from hashlib import md5

import bcrypt
import psycopg2
conn = psycopg2.connect(
    user='postgres',
    host='localhost',
    password='1111',
    database='p11_db')
cur = conn.cursor()


def show_all():
    query = 'select id, name from product'
    cur.execute(query)
    _p = cur.fetchall()
    for i in _p:
        print(f'id: {i[0]}\nname: {i[1]}\n----------------')


def all_info():
    query = 'select * from product'
    cur.execute(query)
    _p = cur.fetchall()
    for i in _p:
        print(f' id: {i[0]}\n name: {i[1]}\n price: {i[2]}\n amount: {i[3]}\n ----------------')


def add_product() -> None:
    _n = input('Name: ')
    _p = int(input('Price: '))
    _a = int(input('Amount: '))
    query = 'insert into product (name, price, amount) values (%s, %s, %s)'
    cur.execute(query, (_n, _p, _a))
    conn.commit()
    print('SUCCESS')


def remove() -> None:
    _id = int(input('Id: '))
    query = f'delete from product where id = {_id}'
    cur.execute(query)
    conn.commit()
    print('SUCCESS')


def change() -> None:
    _id = int(input('id: '))
    _n = input('Name: ')
    _p = int(input('Price: '))
    _a = int(input('Amount: '))
    query = f'update product set name = %s, price = %s, amount = %s where id = %s'
    cur.execute(query, (_n, _p, _a, _id))
    conn.commit()
    print('SUCCESS')


def shop():
    while True:
        title = '''
            1. show all products
            2. all info about products
            3. add product
            4. remove product
            5. change product
            6. exit
        '''
        print(title)
        _c = int(input('Chose: '))
        match _c:
            case 1:
                show_all()
                input()
            case 2:
                all_info()
            case 3:
                add_product()
            case 4:
                remove()
            case 5:
                change()
            case 6:
                break
        input()


def welcome():
    while True:
        title = '''
            1. Login
            2. Signup
            3. exit
        '''
        print(title)
        _c = int(input('Chose: '))
        match _c:
            case 1:
                _u = input('Username: ')
                _p = input('Password: ').encode('utf-8')
                query = 'select password from users where username = %s'
                cur.execute(query, (_u,))
                res = cur.fetchone()
                if res and bcrypt.checkpw(_p, res[0].encode('utf-8')):
                    shop()
                else:
                    print('ERROR')
            case 2:
                _n = input('Name: ')
                _b = input('Birthday: ')
                _u = input('Username: ')
                _p = input('Password: ').encode('utf-8')
                salt = bcrypt.gensalt()
                password = bcrypt.hashpw(_p, salt)
                try:
                    _b = int(_b) if int(_b[0]) else int(_b[1:])
                    query = 'insert into users(name, username, password, birth_date) values (%s, %s, %s, %s)'
                    cur.execute(query, (_n, _u, password.decode(), _b))
                    conn.commit()
                    shop()
                except:
                    print("ERROR")
            case 3:
                break


welcome()
print(type("hello".encode()))
