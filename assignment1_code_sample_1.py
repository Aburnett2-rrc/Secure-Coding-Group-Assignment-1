import os
import pymysql
from urllib.request import urlopen


# Category: Cryptographic Failures, Broken Access Control, Security Misconfiguration, Identification and Authentication Failures
# (does not attempt to prove the identity of the user)

# Password stored in-code, 
# if this were a real password and in a github repository (which it is), 
# it would be visible to everyone who can view the repository.
# Better to store it in secrets or environment variables or something.
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}


# Category: Injection

# User input is not validated at all
# There could at LEAST be a check to make sure it isn't empty
# The user should not be allowed to type whatever they want
# Since this is supposed to be a name presumably,
# there could be a check to ensure the input only contains
# letters of the alphabet
# Possibly also a maximum length
def get_user_input():
    user_input = input('Enter your name: ')
    return user_input


# Category: Injection, Insecure Design

# Any of these parameters could probably be used for malicious purposes
# in the case that the user can imput anything (which is true as seen above),
# the user could inject code into the system command 
# (because it is done with string building/formatting)
def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
