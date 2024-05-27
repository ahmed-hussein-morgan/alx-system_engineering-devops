#!/usr/bin/python3
"""
export data in the JSON format
* Records all tasks from all employees
* Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
* File name must be: todo_all_employees.json

(complete this task -- the below is the code of task 02 to update it)

"""
import json
import requests
import sys

if __name__ == "__main__":
    to_do_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_response = requests.get("https://jsonplaceholder.typicode.com/users")

    todo_json = to_do_response.json()
    user_json = user_response.json()

    user_name = ""
    # task_name = ""
    user_id = sys.argv[1]

    user_tasks = []
    # task_details = {}
    all_data = {}

    for user in user_json:
        if int(user_id) == user.get("id"):
            # get the user name
            user_name = user.get("name")

    for task in todo_json:
        if int(user_id) == task.get("userId"):
            task_details = {}
            task_details["task"] = task.get("title")
            task_details["completed"] = task.get("completed")
            task_details["username"] = user_name
            user_tasks.append(task_details)
    all_data[user_id] = user_tasks

    # print(len(user_tasks))

    with open(f"{user_id}.json", 'w') as file:
        json.dump(all_data, file)
