#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO list progress
Implemented using recursion
"""
import json
import urllib.request

def get_employee_todo_list(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = urllib.request.urlopen(url)
    todos = json.loads(response.read())
    
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = urllib.request.urlopen(employee_url)
    employee = json.loads(employee_response.read())
    name = employee['name']
    
    completed_todos = [todo for todo in todos if todo['completed']]
    num_completed = len(completed_todos)
    num_total = len(todos)
    
    print(f'Employee {name} is done with tasks({num_completed}/{num_total}):')
    for todo in completed_todos:
        print(f'\t{todo["title"]}')

employee_id = input("Enter employee id: ")
get_employee_todo_list(int(employee_id))
