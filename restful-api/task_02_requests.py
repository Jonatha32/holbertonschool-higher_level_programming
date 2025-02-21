#!/usr/bin/python3
import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts/'


def fetch_and_print_posts():
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for i in data:
            print(i['title'])
    else:
        print("Failed to fetch post.")


def fetch_and_save_posts():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        list_ = []
        for i in data:
            list_dic = {
                "id": i["id"],
                "title": i["title"],
                "body": i["body"],
                "userId": i["userId"]
            }
            list_.append(list_dic)

        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title",
                                                      "body", "userId"])
            writer.writeheader()

            for i in list_:
                writer.writerow(i)
    else:
        print("Failed to fetch data.")
