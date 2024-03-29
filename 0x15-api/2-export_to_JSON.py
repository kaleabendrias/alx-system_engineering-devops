#!/usr/bin/python3
"""extend your Python script to export data in the json format"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users/{}".format(url, employee_id))
    todos_response = requests.get("{}/todos?userId={}"
                                  .format(url, employee_id))

    employee_name = user_response.json().get('username')

    todos = todos_response.json()

    data = {employee_id: []}
    for task in todos:
        data[employee_id].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })

    with open("{}.json".format(employee_id), 'w') as file:
        json.dump(data, file)
