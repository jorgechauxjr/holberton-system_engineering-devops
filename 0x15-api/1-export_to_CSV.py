#!/usr/bin/python3
"""Export data in the CSV format"""

import csv
import requests
from sys import argv


def to_do_list(user_id):
    """retireve the toDo list"""
    url = 'https://jsonplaceholder.typicode.com/'
    user_request = "{}users/{}".format(url, user_id)
    employee_dict = requests.get(user_request).json()
    employee_name = employee_dict.get("name")

    tasks_dict = requests.get("{}todos?userId={}".format(url, user_id)).json()
    user_name = employee_dict.get("username")

    file_name = "{}.csv".format(user_id)

    with open(file_name, mode='w') as csv_file:
        csvWriter = csv.writer(csv_file)
        for info in tasks_dict:
            csvWriter.writerow([user_id, user_name,
                               info.get("completed"), info.get("title")])

if __name__ == "__main__":
    to_do_list(argv[1])
