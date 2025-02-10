#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import sys
import requests

if __name__ == "__main__":
    user_id = int(sys.argv[1])  # Convert to integer
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(f"{url}users/{user_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    completed = [t["title"] for t in todos if t["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(completed), len(todos)))

    for task in completed:
        print("\t{}".format(task))  # Ensure correct formatting
