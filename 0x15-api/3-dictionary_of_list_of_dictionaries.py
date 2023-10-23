#!/usr/bin/python3
"""extend your Python script to export data in the json format"""
import json
import requests


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = base_url + 'users'
    response = requests.get(users_url)
    users = response.json()

    todo_all_employees = {}
    for user in users:
        user_id = str(user['id'])
        todos_url = base_url + 'todos?userId=' + user_id
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        task_list = []
        for task in todos_data:
            task_dict = {"username": user['username'],
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            task_list.append(task_dict)

        todo_all_employees[user_id] = task_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_all_employees, json_file)
