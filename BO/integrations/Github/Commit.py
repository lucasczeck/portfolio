import requests

from core.integracoes.github.models import Commits


class Commit:

    def __init__(self, urls):
        self.urls = urls

    @staticmethod
    def get_repository_commits(url):
        response = requests.get(url)
        data = response.json()

        return data, url

    @staticmethod
    def check_commit(commit):
        Commits.objects.filter(sha=commit.get('sha'))