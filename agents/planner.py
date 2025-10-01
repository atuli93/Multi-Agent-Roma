"""
Planner Agent for Multi-Agent ROMA Workflow Hub
This version uses a mock planner for demo purposes (no OpenAI API required).
"""

def breakdown(goal):
    """
    Mock Planner for demo purposes.
    Returns 5 subtasks instantly without hitting OpenAI API.
    """
    return [
        "Task 1: Research topic",
        "Task 2: Create outline",
        "Task 3: Write content",
        "Task 4: Review draft",
        "Task 5: Publish final version"
    ]
