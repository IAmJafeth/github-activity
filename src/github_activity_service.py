import requests

GITHUBAPI_URL: str = "https://api.github.com/users/{username}/events?per_page={limit}"
ACTIVITY_TYPE = dict[str, dict[str, list[dict]]]


def fetch_github_activity(username: str, limit: int) -> list[dict]:
    try:
        response = requests.get(GITHUBAPI_URL.format(username=username, limit=limit))
    except requests.exceptions.RequestException as e:
        print("Unable to fetch GitHub activity, check your internet connection.")
        raise e

    if response.status_code == 404:
        print("Username", username, "not found")
        raise requests.exceptions.RequestException("Username not found")
    elif 500 <= response.status_code <= 511:
        print("Server error", response.status_code)
        raise requests.exceptions.RequestException("Server error")

    return response.json()


def parse_github_activity(github_http_response: list[dict]) -> ACTIVITY_TYPE:
    activity: ACTIVITY_TYPE = {}

    for event in github_http_response:
        repo_name = event['repo']['name']
        if activity.get(repo_name) is None:
            activity[repo_name] = {}

        event_type = event['type']
        payload = event['payload']
        if activity[repo_name].get(event_type) is None:
            activity[repo_name][event_type] = []
            activity[repo_name][event_type].append(payload)
        else:
            activity[repo_name][event_type].append(payload)

    return activity

def count_push_events(activity: ACTIVITY_TYPE) -> dict[str, int]:
    push_events: dict[str, int] = {}
    for repo in activity:
        push_events[repo] = 0
        for _ in activity[repo].get('PushEvent', []):
            push_events[repo] += 1

    return push_events

def parse_push_events(activity: ACTIVITY_TYPE) -> str:
    push_events = count_push_events(activity)
    parsed_push_events: str = ""
    for repo, count in push_events.items():
        if count > 0:
            parsed_push_events += f"- Pushed {count} commits to {repo}\n"

    return parsed_push_events

def parse_issue_event(event: dict) -> str:
    match event['action']:
        case "opened":
            return f"- Opened Issue #{event['issue']['number']}"
        case "closed":
            return f"- Closed Issue #{event['issue']['number']}"
        case "reopened":
            return f"- Reopened Issue #{event['issue']['number']}"
        case _:
            return f"- Updated Issue #{event['issue']['number']}"

def parse_issuecomment_event(event: dict) -> str:
    match event['action']:
        case "created":
            return f"- Commented on Issue #{event['issue']['number']}"
        case _:
            return f"- Updated Comment on Issue #{event['issue']['number']}"


def parse_member_event(event: dict) -> str:
    match event['action']:
        case "added":
            return f"- Added {event['member']['login']}"
        case _:
            return f"- Removed {event['member']['login']}"

def parse_create_event(event: dict, repo_name: str) -> str:
    if event["ref_type"] == "repository":
        return f"- Created Repository {repo_name}"
    else:
        return f"- Created {event['ref_type']} {event['ref']} in {repo_name}"