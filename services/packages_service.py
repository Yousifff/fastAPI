from typing import List
def release_count()-> int:
    return 2_345_678


def package_count()->int:
    return 2000


def latest_packages(limit:int=5)->List:
    return [
        {'id': 'fastapi', 'summary': 'A great web framework'},
        {'id': 'uvicorn', 'summary': 'Your favorite ASGI server'},
        {'id': 'httpx', 'summary': 'Requests for an async world'},
    ][:limit]