import requests

from core.integracoes.github.models import Commits, Repositories


class Commit:

    def __init__(self, urls):
        self.urls = urls
        self.list_commits = []

    @staticmethod
    def get_repository_commits(url):
        data = []
        response = requests.get(url)
        commits = response.json()

        for commit in commits:
            if 'Merge branch' not in commit['commit']['message']:
                data.append(commit)

        return data

    @staticmethod
    def check_commit(sha):
        commit = Commits.objects.filter(sha=sha).first()
        if commit:
            status = False
        else:
            status = True

        return status

    @staticmethod
    def create_commit(data, repository_id):
        commit = Commits()
        commit.sha = data.get('sha')
        commit.date = data.get('commit').get('committer').get('date')
        commit.message = data.get('commit').get('message')
        commit.url = data.get('url')
        commit.repository_id = repository_id
        commit.save()

        return commit

    def update_commits(self):
        for url in self.urls:
            repository = Repositories.objects.filter(commits_url=url).first()
            data = self.get_repository_commits(url)
            for commit in data:
                is_create = self.check_commit(commit.get('sha'))

                if is_create:
                    commit_created = self.create_commit(commit, repository.id)
                    if commit_created:
                        self.list_commits.append(commit_created)

        return self.format_response()

    def format_response(self):
        list_create = []
        for commit in self.list_commits:
            message = f'O commit de sha {commit.sha}, feito em {commit.date} foi criado com sucesso!'
            list_create.append(message)

        response = {'criados': list_create}

        return response
