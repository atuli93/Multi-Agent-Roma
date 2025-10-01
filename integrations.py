from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_API_KEY"))

def push_to_notion(database_id, tasks):
    for task in tasks:
        if task.strip():
            notion.pages.create(
                parent={"database_id": database_id},
                properties={"Name": {"title":[{"text":{"content":task}}]}}
            )
