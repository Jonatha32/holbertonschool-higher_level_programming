#!/usr/bin/python3
import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts/'


def fetch_and_print_posts():
    response = requests.get(url)
    if response.status_code == 200:
        data = data.json()
        for i in data:
            print(i['title'])
    else:
        print("Failed to fetch post.")


def fetch_and_save_post():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        list_ = []
        for i in data:
            list_dic = {
                "id": i["id"],
                "title": i["title"],
                "body": i["body"]
            }
            list_.append(list_dic)

        with open('posts.csv', mode='w', newline='') as file:
            a = ['id', 'title', 'body']
            writer = csv.DictWriter(file, a=a)

            writer.writeheader()
            writer.writerows(list_)

        print("Data successfully saved to post.csv")
    else:
        print("Failed to fetch data.")
