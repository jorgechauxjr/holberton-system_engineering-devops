#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
from sys import argv

url = 'https://jsonplaceholder.typicode.com/'


def get_username(user_id):
    """Return the username"""

    user_request = "{}users/{}".format(url, user_id)
    employee_dict = requests.get(user_request).json()
    employee_username = employee_dict.get("username")
    return employee_username


def search_and_export_json():
    """Export data in the JSON format"""

    tasks_dict = requests.get("{}todos".format(url)).json()

    my_dict = {}
    my_list = []

    for info in tasks_dict:
        tasks_all_emp = {}
        tasks_all_emp["task"] = info.get('title')
        tasks_all_emp["completed"] = info.get('completed')
        id = info.get('userId')
        username = get_username(id)
        tasks_all_emp["username"] = username
        my_list.append(tasks_all_emp)

    my_dict["1"] = my_list

    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as json_file:
        json.dump(my_dict, json_file)

if __name__ == "__main__":
    search_and_export_json()
