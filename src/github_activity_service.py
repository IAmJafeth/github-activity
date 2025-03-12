import requests
from pprint import pprint

GITHUBAPI_URL: str = "https://api.github.com/users/{username}/events?per_page={limit}"
ACTIVITY_TYPE = dict[str, dict[str, list[dict]]]


def fetch_github_activity(username: str, limit: int) -> list[dict]:
    return requests.get(GITHUBAPI_URL.format(username=username, limit=limit)).json()


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

def parse_issue_events(activity: ACTIVITY_TYPE) -> str:
    """TODO"""

def parse_issuecomment_events(activity: ACTIVITY_TYPE) -> str:
    """TODO"""

def parse_create_events(activity: ACTIVITY_TYPE) -> str:
    """TODO"""

def parse_member_events(activity: ACTIVITY_TYPE) -> str:
    """TODO"""


# list all distinct events
def list_events(activity: ACTIVITY_TYPE) -> str:
    events: set[str] = set()
    for repo in activity:
        for event in activity[repo]:
            events.add(event)

    return "\n".join(events)

def get_payload(activity: ACTIVITY_TYPE, event_type: str) :
    for repo in activity:
        for event in activity[repo]:
            if event == event_type:
                return activity[repo][event]

def main():
    activity = fetch_github_activity("IAmJafeth", 100)
    parsed_activity = parse_github_activity(activity)
    pushed_events = parse_push_events(parsed_activity)
    print(list_events(parsed_activity))
    pprint(get_payload(parsed_activity, "IssuesEvent"))


if __name__ == '__main__':
    main()