from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def breakdown(goal):
    """
    Uses AI model (Dobby/GPT) to break a goal into 5 actionable subtasks
    """
    prompt = f"Break this goal into 5 actionable subtasks:\n\n{goal}"
    response = client.chat.completions.create(
        model="dobby-70b",  # or the correct model name
        messages=[{"role":"user","content":prompt}]
    )
    tasks = [t.strip() for t in response.choices[0].message.content.split("\n") if t]
    return tasks
