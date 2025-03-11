import argparse

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='github-activity',
        description='Simple CLI tool to fetch Github Activity',
        epilog='A Roadmap.sh Project | Created by: @IAmJafeth'
    )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')
    parser.add_argument("gh_user", help="Github User to fetch activity")
    parser.add_argument('-l', '--limit', type=int, help="Limit the number of events to fetch DEFAULT=15 MAX=100", default=15)

    return parser



