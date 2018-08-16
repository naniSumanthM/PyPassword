"""
Script provides functions that help interact with the Sqlite db
and make a HTTP get request
"""

# dependencies
import sqlite3
from sqlite3 import Error
import requests
import password_generator
import random
from user import *

"""
connect_to_sqlite function connects to the database

Args:
db_source - file path to the sqlite file

Returns: connection object
"""


def connect_to_sqlite(db_source: str):
    try:
        connection = sqlite3.connect(db_source)
    except Error as e:
        print(e)
    return connection


"""
fetch_user invokes an HTTP get to fetch a random user from the endpoint: https://randomuser.me/api/
a randomly generated password is also generated and passed to the user object constructor

Args:
None

Returns: user object with properties (user_name, user_email, user_password)
"""


def fetch_user() -> user:
    generate_user = requests.get('https://randomuser.me/api/')

    if generate_user.status_code == 200:
        data = generate_user.json()
        random_fullname = data['results'][0]['name']['first'] + \
            ' ' + data['results'][0]['name']['last']
        random_email = data['results'][0]['email']
        random_password = password_generator.generate_password(random.randint(6, 12), random.randint(1, 4))
        new_user = user(random_fullname, random_email, random_password)
        return new_user
    else:
        print(generate_user.status_code + '-Error')


"""
insert_user function inserts a new user into the database
prints the newly inserted user onto the console

Args:
user_name is the full name of the user
user_email is the email of the user

Returns:
None
"""


def insert_user(user_name, user_email) -> None:
    connection = connect_to_sqlite('./User.sqlite')
    sqlite_client = connection.cursor()

    create_table = 'CREATE TABLE IF NOT EXISTS {tn} (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, user_name VARCHAR(255), user_email VARCHAR(255))' \
        .format(tn="tbl_user")

    insert_record = (
        "INSERT INTO {tn} ({col_1}, {col_2}) VALUES ('{value_1}','{value_2}')". format(
            tn="tbl_user",
            col_1="user_name",
            col_2="user_email",
            value_1=user_name,
            value_2=user_email))

    select_all = "SELECT * FROM tbl_user"

    try:
        sqlite_client.execute(create_table)
        sqlite_client.execute(insert_record)
        sqlite_client.execute(select_all)
        all_rows = sqlite_client.fetchall()
        print(all_rows)
    except Error as e:
        print(e)
    finally:
        sqlite_client.close()


"""
insert_mass_users function inserts 10 random user objects into the database
and prints the records from the database to the console

The function randomly generates 10 users using a for loop
and generates a random password using the generate_password function
with a randomly chosen password length and complexity

Args:
none

Returns:
None
"""


def insert_mass_users() -> None:
    connection = connect_to_sqlite('./User.sqlite')
    sqlite_client = connection.cursor()

    create_table = 'CREATE TABLE IF NOT EXISTS {tn} (id INT AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(255), user_email VARCHAR(255), user_password VARCHAR(255))' \
        .format(tn="tbl_rnd_users")
    sqlite_client.execute(create_table)

    for user in range(11):
        rnd_user = fetch_user()

        insert_record = (
            "INSERT INTO {tn} ({col_1}, {col_2}, {col_3}) VALUES ('{value_1}','{value_2}','{value_3}')". format(
                tn="tbl_rnd_users",
                col_1="user_name",
                col_2="user_email",
                col_3='user_password',
                value_1=rnd_user.get_user_name(),
                value_2=rnd_user.get_user_email(),
                value_3=rnd_user.get_user_password()))
        sqlite_client.execute(insert_record)

    select_all = "SELECT * FROM tbl_rnd_users"
    try:
        sqlite_client.execute(select_all)
        all_rows = sqlite_client.fetchall()
        for record in all_rows:
            print(record)
    except Error as e:
        print(e)
    finally:
        sqlite_client.close()


# Invoke functions
new_user = fetch_user()
insert_user(new_user.get_user_name(), new_user.get_user_email())
insert_mass_users()
