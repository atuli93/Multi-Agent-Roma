def review(results):
    """
    Reviews task execution results and returns a summary string.
    """
    summary = "\n".join([f"{task}: {status}" for task, status in results.items()])
    return f"Workflow Review:\n{summary}"
