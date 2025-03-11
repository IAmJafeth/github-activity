import sys

import requests
from pprint import pprint

GITHUBAPI_URL: str = "https://api.github.com/users/{username}/events?per_page={limit}"



def fetch_github_activity(username: str, limit: int) -> list[dict]:
    return requests.get(GITHUBAPI_URL.format(username=username, limit=limit)).json()

def parse_github_activity(github_http_response: list[dict]) -> dict[str, dict[str, list[dict]]]:
    activity: dict[str, dict[str, list[dict]]] = {}
    for event in github_http_response:
        repo_name = event['repo']['name']
        if activity.get(repo_name) is None:
            activity[repo_name] = {}

        event_type = event['type']
        if activity[repo_name].get(event_type) is None:
            activity[repo_name][event_type] = []
            activity[repo_name][event_type].append(event['payload'])
        else:
            activity[repo_name][event_type].append(event['payload'])

    return activity

def count_push_events(activity: dict[str, dict[str, list[dict]]]) -> dict[str, int]:
    push_events: dict[str, int] = {}
    for repo in activity:
        push_events[repo] = 0
        for event in activity[repo].get('PushEvent', []):
            push_events[repo] += 1

    return push_events
