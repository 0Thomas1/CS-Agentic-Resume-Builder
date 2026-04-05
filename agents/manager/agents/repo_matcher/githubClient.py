import json
import os
import requests
import base64


class GitApiClient:
    def __init__(self, username, token):
        self.cache_file = os.path.join(os.path.dirname(__file__), "repos.json")
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"
        self.timeout_seconds = 10
        self.max_retries = 3
        self.repos = None

    def _headers(self):
        headers = {"Accept": "application/vnd.github+json"}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    def _request_json(self, url):
        last_error = None
        for _attempt in range(self.max_retries):
            try:
                response = requests.get(url, headers=self._headers(), timeout=self.timeout_seconds)
                if response.status_code == 200:
                    return response.json(), 200
                if response.status_code in (404, 401, 403):
                    return None, response.status_code
                if response.status_code >= 500:
                    last_error = ValueError(f"GitHub API temporary failure: {response.status_code}")
                    continue
                return None, response.status_code
            except requests.RequestException as exc:
                last_error = exc

        if last_error:
            print(f"GitHub API request failed after retries for {url}: {last_error}")
        return None, None

    def get_repositories(self):
        if self.repos is not None:
            return self.repos

        try:
            with open(self.cache_file, 'r') as f:
                self.repos = json.load(f)
                return self.repos
        except (FileNotFoundError, json.JSONDecodeError):
            print("Cache not found or invalid. Fetching repositories from GitHub API...")

        if not self.username:
            print("GITHUB_USERNAME is not configured.")
            self.repos = {}
            return self.repos

        self.repos = {}
        url = f"{self.base_url}/users/{self.username}/repos"
        data, status_code = self._request_json(url)
        if status_code == 200 and isinstance(data, list):
            for repo in data:
                readme = self.get_github_readme(repo['name'])
                languages = self.get_github_repository_languages(repo['name'])
                self.repos[repo['id']] = {
                    "name": repo['name'],
                    "created_at": repo['created_at'],
                    "html_url": repo['html_url'],
                    "readme": readme,
                    "languages": languages
                }

            with open(self.cache_file, 'w') as f:
                json.dump(self.repos, f, indent=4)
            return self.repos
        else:
            print(f"Failed to fetch repositories. Status code: {status_code}")
            return self.repos

    # get repository languages
    def get_github_repository_languages(self, repo_name):
        url = f"https://api.github.com/repos/{self.username}/{repo_name}/languages"
        data, status_code = self._request_json(url)
        if status_code == 200 and isinstance(data, dict):
            return data
        return {}

    # get github readme for a repository
    def get_github_readme(self, repo_name):
        url = f"https://api.github.com/repos/{self.username}/{repo_name}/readme"
        data, status_code = self._request_json(url)
        if status_code == 200 and isinstance(data, dict):
            content = data.get('content')
            if content:
                try:
                    return base64.b64decode(content).decode('utf-8')
                except ValueError:
                    return f"README decoding failed for repository {repo_name}."
            return f"README content missing for repository {repo_name}."
        if status_code == 404:
            return f"README not found for repository {repo_name}."
        return f"README unavailable for repository {repo_name}."
    