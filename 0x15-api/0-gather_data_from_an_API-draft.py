#!/usr/bin/python3
"""
generate demo data using REST API of a todo list

print first line in the following formate:
Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS)

"""
import requests
import sys

if __name__ == "__main__":
    to_do_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_response = requests.get("https://jsonplaceholder.typicode.com/users")
    # decoded_response = response.content.decode()
    # print(type(decoded_response))
    # print(decoded_response)

    # for task in decoded_response:
    #     print(task)

    print(type(to_do_response))
    # print(response.json())

    # print item in dictionary

    for item in to_do_response.json():
        print(item)
    print("########################################################################")
    print("########################################################################")
    print("########################################################################")
    for item in user_response.json():
        print(item)
