import parser_service
import github_activity_service

def main():
    """Entry point of the program."""
    parser = parser_service.get_parser()
    args = parser.parse_args()

    try:
        raw_activity = github_activity_service.fetch_github_activity(args.gh_user, args.limit)
    except Exception as e:
        parser.exit(status=1, message=str(e))

    activity = github_activity_service.parse_github_activity(raw_activity)

    parsed_events = ""
    parsed_events += github_activity_service.parse_push_events(activity)

    for repo in activity:
        for event_type in activity[repo]:
            for event in activity[repo][event_type]:
                match event_type:
                    case "IssuesEvent":
                        parsed_events += github_activity_service.parse_issue_event(event) + f" in {repo}\n"
                    case "IssueCommentEvent":
                        parsed_events += github_activity_service.parse_issuecomment_event(event) + f" in {repo}\n"
                    case "MemberEvent":
                        parsed_events += github_activity_service.parse_member_event(event) + f" in {repo}\n"
                    case "CreateEvent":
                        parsed_events += github_activity_service.parse_create_event(event, repo) + "\n"
                    case "PushEvent":
                        pass
                    case _:
                        parsed_events += f"- {event_type} in {repo}\n"

    print(parsed_events)

if __name__ == '__main__':
    main()
