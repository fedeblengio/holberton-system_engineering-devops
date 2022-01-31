#!/usr/bin/python3
'''asjnhdjnasdjnasdjnjandasjndjansdnj'''
import requests
from sys import argv

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + f"users?id={argv[1]}")
    tasks = requests.get(url + f"todos?userId={argv[1]}")

    userJson = user.json()
    tasksJson = tasks.json()
    userName = userJson[0]["name"]
    completedTasks = 0

    for i in tasksJson:
        if i['completed']:
            completedTasks += 1

    print("Employee {} is done with tasks({}/{}): ".format(
        userName, completedTasks, len(tasksJson)))

    for i in tasksJson:
        if i['completed']:
            print("\t {}".format(i.get('title')))
