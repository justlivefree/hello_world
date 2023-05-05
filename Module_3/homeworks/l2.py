from psycopg2 import connect
from psycopg2.extras import DictCursor
from typing import Optional
from bcrypt import hashpw, checkpw, gensalt

conn = connect(
    database='p11_db',
    user='postgres',
    password='1111',
    host='localhost',
    cursor_factory=DictCursor)

cur = conn.cursor()


def make_hash(password: str) -> str:
    _password = password.encode('utf-8')
    salt = gensalt()
    return hashpw(_password, salt).decode()


def check_hash(password: str, hashed: str):
    _hashed = hashed.encode('utf-8')
    _password = password.encode('utf-8')
    return checkpw(_password, _hashed)


def find_user(username: str = '', password: str = '') -> Optional[tuple]:
    query = "select id, is_admin, password from users where username='{0}'".format(username)
    cur.execute(query)
    get_info = cur.fetchone()
    if get_info and check_hash(password, get_info['password']):
        return get_info[:-1]
    else:
        return None


def add_user(name: str, username: str, password: str, year: int) -> bool:
    _password = make_hash(password)
    if not find_user(username=username, exist=False):
        query = 'insert into users(is_admin, name, username, password, year) ' \
                'values (false, %s, %s, %s, %s);'
        cur.execute(query, (name, username, _password, year))
        conn.commit()
        return True
    return False


class Admin:
    def __init__(self):
        print('that is admin')


class User:
    def __init__(self):
        print('that is user')


def welcome():
    title = '''
    1. Login
    2. Signup
    3. exit
    '''
    print(title)
    try:
        chose = int(input('Chose: '))
        match chose:
            case 1:
                username = input('Username: ')
                password = input('Password: ')
                get_info = find_user(username, password)
                if get_info:
                    Admin() if get_info[1] else User()
                else:
                    print('Invalid password or username!')
            case 2:
                name = input('Name: ')
                year = int(input('Birth year: '))
                username = input('Username: ')
                password = input('Password: ')
                if add_user(name, username, password, year):
                    User()
                else:
                    print('This username already exist!')
    except ValueError:
        welcome()
    input()
    welcome()


welcome()
