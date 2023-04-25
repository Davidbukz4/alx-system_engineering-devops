#!/usr/bin/python3
'''
A module taht interact with REST API
'''
import requests
import sys


api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    try:
        employee_id = int(sys.argv[1])
        user_info = requests.get('{}/users/{}'.format(api, employee_id))
        employee_name = user_info.json().get('name')
        todos_info = requests.get('{}/todos'.format(api)).json()
        done_todo = []
        undone_todo = []
        for info in todos_info:
            if info['userId'] == employee_id:
                if info['completed']:
                    done_todo.append(info['title'])
                else:
                    undone_todo.append(info['title'])
        done = len(done_todo)
        undone = len(undone_todo)
        print('Employee {} is done with tasks({}/{}):'
              .format(employee_name, done, undone + done))
        for todo in done_todo:
            print('\t ' + todo)
    except Exception:
        pass
