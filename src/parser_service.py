import argparse

def get_parser() -> argparse.ArgumentParser:
    GITHUB_API_DISCLAIMER = "This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h."

    parser = argparse.ArgumentParser(
        prog='github-activity',
        description='Simple CLI tool to fetch Github Activity',
        epilog=' API DISCLAIMER: ' + GITHUB_API_DISCLAIMER + ' | A Roadmap.sh Project | Created by: @IAmJafeth'
    )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')
    parser.add_argument("gh_user", help="Github User to fetch activity")
    parser.add_argument('-l', '--limit', type=int, help="Limit the number of events to fetch DEFAULT=15 MAX=100", default=15)

    return parser



