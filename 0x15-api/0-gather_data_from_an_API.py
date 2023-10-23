#!/usr/bin/python3
""" REST API, for a given employee ID, returns information about """
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{url}/users/{employee_id}")
    todos_response = requests.get(f"{url}/todos?userId={employee_id}")

    employee_name = user_response.json().get('name')
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo["completed"]]
    num_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks(\
{num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")
