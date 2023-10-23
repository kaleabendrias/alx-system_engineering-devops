#!/usr/bin/python3
"""extend your Python script to export data in the json format"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{url}/users/{employee_id}")
    todos_response = requests.get(f"{url}/todos?userId={employee_id}")

    employee_name = user_response.json().get('username')

    todos = todos_response.json()

    data = {employee_id: []}
    for task in todos:
        data[employee_id].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })

    with open(f"{employee_id}.json", 'w') as file:
        json.dump(data, file)
