from core.integracoes.github.models import Repositories


class Repository:

    def __init__(self, itens):
        self.items = itens
        self.repositories = self.get_list_repositories()

    @staticmethod
    def get_list_repositories():
        repositories = list(Repositories.objects.active().all().values_list('id', flat=True))

        return repositories

    def check_repositories(self):
        list_repositories = []
        list_disabled = []
        for item in self.items:
            list_repositories.append(item.get('id'))

        for repository in self.repositories:
            if repository not in list_repositories:
                self.disable_repository(repository)
                list_disabled.append(repository)

    def disable_repository(self, id):
        repository = self.find_repository(id)
        repository.disable()

    @staticmethod
    def find_repository(id):
        repository = Repositories.objects.filter(id=id).first()

        return repository

    @staticmethod
    def create_repository(data):
        repository = Repositories()
        repository.id = data.get('id')
        repository.name = data.get('name')
        repository.is_private = True if data.get('private') is True else False
        repository.commits_url = data.get('commits_url')
        repository.created_date = data.get('created_at')
        repository.pushed_date = data.get('pushed_at')
        repository.save()

        return True, repository
