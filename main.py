from agents.planner import breakdown
from agents.executor import execute
from agents.reviewer import review
# Optional: from utils.integrations import push_to_notion
import os

goal = "Launch a content marketing campaign"

tasks = breakdown(goal)
print("Planner Output:", tasks)

results = execute(tasks)
print("Executor Results:", results)

summary = review(results)
print(summary)

# Optional: push to Notion
# push_to_notion(os.getenv("NOTION_DATABASE_ID"), tasks)
