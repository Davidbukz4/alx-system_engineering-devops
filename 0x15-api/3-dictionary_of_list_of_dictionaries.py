#!/usr/bin/python3
'''
A module that interact with REST API
'''
import json
import requests


api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    try:
        users_info = requests.get('{}/users'.format(api)).json()
        todos_info = requests.get('{}/todos'.format(api)).json()
        todo_list = []
        all_data = {}
        file_name = 'todo_all_employees.json'
        for user in users_info:
            user_name = user.get('username')
            user_id = user.get('id')
            for info in todos_info:
                if info.get('userId') == user_id:
                    todo_list.append(info)
                data = list(map(
                        lambda x: {
                            "username": user_name
                            "task": x.get("title"),
                            "completed": x.get("completed"),
                        }, todo_list))
                data = {'{}'.format(user_id): data}
                all_data.update(data)
        with open(file_name, 'w') as f:
            json.dump(all_data, f)
    except Exception as e:
        print(e)
