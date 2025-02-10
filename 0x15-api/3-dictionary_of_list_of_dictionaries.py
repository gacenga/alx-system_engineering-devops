#!/usr/bin/python3

"""

    API that fetches info about to do list

"""

import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com'

def get_to_do():
   """ gets employee name and tasks """
   emp_rq = requests.get(f"{base_url}/users/")
   todo_rq = requests.get(f"{base_url}/todos?userid={employee_id}")

   if emp_rq.status_code != 200 or todo_rq.status_code != 200:
       print("Error fetching data")
       return

   emp = emp_rq.json()
   todo = todo_rq.json()

   emp_name = emp.get("name")
   total_todo = len(todo)
   done_todo = [n for n in todo if n.get("completed")]

if __name__ == '__main__':
    get_to_do()
