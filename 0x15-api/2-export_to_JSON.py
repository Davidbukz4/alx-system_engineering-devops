#!/usr/bin/python3
'''
A module that interact with REST API
'''
import json
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
        todo = ''
        with open('{}.json'.format(employee_id), 'w') as f:
            data = list(map(
                       lambda x: {
                            "task": x.get("title"),
                            "completed": x.get("completed"),
                            "username": user_name
                        }, todo_list))
            data =  {'{}'.format(employee_id): data}
            json.dump(data, f)
    except Exception:
        pass
