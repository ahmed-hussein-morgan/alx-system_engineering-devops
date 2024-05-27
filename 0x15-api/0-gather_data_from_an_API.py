#!/usr/bin/python3
"""
generate demo data using REST API of a todo list

print first line in the following formate:
Employee EMPLOYEE_NAME is done with tasks
    (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS)

"""
import requests
import sys

if __name__ == "__main__":
    to_do_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_response = requests.get("https://jsonplaceholder.typicode.com/users")

    todo_json = to_do_response.json()
    user_json = user_response.json()

    user_name = ""
    task_name = ""
    completed_tasks = 0
    total_tasks = 0
    user_id = int(sys.argv[1])
    tasks_title = []

    for user in user_json:
        if user_id == user.get("id"):
            user_name = user.get("name")

    for task in todo_json:
        if user_id == task.get("userId"):
            total_tasks += 1
            if task.get("completed") is True:
                completed_tasks += 1
                tasks_title.append(task)

    print("Employee {} is done with \
tasks({}/{}):".format(user_name, completed_tasks, total_tasks))
    for complete in tasks_title:
        print("\t", complete.get("title"))
