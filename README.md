# [GitHub Activity CLI](https://roadmap.sh/projects/github-user-activity)

## Overview
This project is a simple command-line interface (CLI) application that fetches and displays the recent activity of a specified GitHub user. It helps practice working with APIs, handling JSON data, and building CLI applications.

## Features
- Accepts a GitHub username as an argument.
- Fetches the user's recent activity from the GitHub API.
- Displays the fetched activity in the terminal in a readable format.
- Handles errors gracefully, such as invalid usernames or API failures.
- Built without external libraries or frameworks for API requests.

## Usage

Clone the repository:
```sh
git clone https://github.com/IAmJafeth/github-activity.git
```

Navigate to the project directory:
```sh
cd github-activity
```

Install the packages:
```sh
pip install .
````

Run the CLI with a GitHub username as an argument:
```sh
github-activity <username>
```

## Example Output
```sh
- Pushed 3 commits to iamjafeth/repo-name
- Opened a new issue in iamjafeth/repo-name
- Starred iamjafeth/repo-name
```

## API Endpoint
The application fetches data from:
```
https://api.github.com/users/<username>/events
```
Example:
```
https://api.github.com/users/iamjafeth/events
```

## Future Enhancements
For an advanced version, consider adding:
- Filtering activity by event type.
- Structured output formatting.
- Caching fetched data for performance improvement.
- Fetching additional user or repository details.

## References
- [GitHub API Documentation](https://docs.github.com/en/rest)

---

Happy coding! 🚀