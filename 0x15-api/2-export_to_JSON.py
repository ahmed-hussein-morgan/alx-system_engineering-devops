#!/usr/bin/python3
"""
export data to json file
{ "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"},
 {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
   "username": "USERNAME"}, ... ]}
 File: 2-export_to_JSON.py
example:
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt",
 "completed": false, "username": "Antonette"},
{"task": "distinctio vitae autem nihil ut molestias quo",
 "completed": true, "username": "Antonette"},
{"task": "et itaque necessitatibus maxime molestiae qui quas velit",
 "completed": false, "username": "Antonette"}]}
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
    task_name = ""
    user_id = sys.argv[1]

    user_tasks = []
    task_details = {}
    all_data = {}

    for user in user_json:
        if int(user_id) == user.get("id"):
            # get the user name
            user_name = user.get("name")

    for task in todo_json:
        if int(user_id) == task.get("userId"):
            task_details["task"] = task.get("title")
            task_details["completed"] = task.get("completed")
            task_details["username"] = user_name
        user_tasks.append(task_details)
    all_data[user_id] = user_tasks

    with open(f"{user_id}.json", 'w') as file:
        json.dump(all_data, file)
