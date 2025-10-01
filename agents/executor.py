def execute(tasks):
    """
    Simulates executing each task.
    Returns a dictionary of results.
    """
    results = {}
    for task in tasks:
        results[task] = f"{task} ✅ completed"
    return results
