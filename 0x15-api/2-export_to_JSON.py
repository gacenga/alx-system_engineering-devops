#!/usr/bin/python3

"""

    API that fetches info about to do list

"""

import requests
import sys
import json

base_url = 'https://jsonplaceholder.typicode.com'

def get_to_do(employee_id):
   """ gets employee name and tasks """
   emp_rq = requests.get(f"{base_url}/users/{employee_id}")
   todo_rq = requests.get(f"{base_url}/todos?userid={employee_id}")

   if emp_rq.status_code != 200 or todo_rq.status_code != 200:
       print("Error fetching data")
       return

   emp = emp_rq.json()
   todo = todo_rq.json()

   emp_name = emp.get("name")
   total_todo = len(todo)

   json_filename = f"{employee_id}.json"
   data = { f"{employee_id}": [{"task": f'{n.get("title")}', "completed": n.get("completed"), "username": f"{emp_name}"} for n in todo]}
   with open(json_filename, mode='w') as file:
       json.dump(data, file)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_to_do(employee_id)
    except ValueError:
        print("Employee id must be integer")
