#!/usr/bin/python3
'''
A module that interact with REST API
'''
import requests
import sys


api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    try:
        employee_id = int(sys.argv[1])
        user_info = requests.get('{}/users/{}'.format(api, employee_id))
        user_name = user_info.json().get('username')
        todos_info = requests.get('{}/todos'.format(api)).json()
        todo_list = []
        for info in todos_info:
            if info.get('userId') == employee_id:
                todo_list.append(info)
        with open('{}.csv'.format(employee_id), 'w') as f:
            for todo in todo_list:
                f.write('"{}","{}","{}","{}"\n'.format(employee_id, user_name,
                        todo.get('completed'), todo.get('title')))
    except Exception:
        pass
