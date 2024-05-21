#!/usr/bin/python3
"""
gather fak data using api
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    # URL template for fetching employee data
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
        return
    
    todos = response.json()
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])
    
    print(f"Employee {todos[0]['title']} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print("\t", todo['title'])

if __name__ == "__main__":
    if len(sys.argv)!= 2:
        print("Usage: python script.py <EMPLOYEE_ID>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

