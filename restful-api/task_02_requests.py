import requests
import csv

"""Module to fetch posts from JSONPlaceholder using requests.get()"""


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints them to the console."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"{post['title']}, {post['body']}")


def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder and saves them to a CSV file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["id", "title", "body"])
            for post in posts:
                writer.writerow([post['id'], post['title'], post['body']])
