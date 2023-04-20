from core.integracoes.github.models import Repositories


class Repository:

    def __init__(self, items):
        self.list_disabled = []
        self.list_update = []
        self.items = items
        self.repositories = self.get_list_repositories()
        self.check_repositories()

    @staticmethod
    def get_list_repositories():
        repositories = list(Repositories.objects.active().all().values_list('id', flat=True))

        return repositories

    @staticmethod
    def get_list_urls():
        urls = list(Repositories.objects.active().all().values_list('commits_url', flat=True))

        return urls

    @staticmethod
    def format_response(return_list):
        created = []
        updated = []
        desabled = []

        for message in return_list:
            if 'criado' in message:
                created.append(message)
            elif 'atualizado' in message:
                updated.append(message)
            else:
                desabled.append(message)

        response = {'Criados': created, 'Atualizados': updated, 'Desativados': desabled}

        return response

    def update_repositories(self):
        return_list = []
        for item in self.items:
            status, repository, is_created = self.manage_repository(data=item)
            if is_created:
                message = f'O repositório {repository.name} foi criado com o id: {repository.id}'
                return_list.append(message)
            else:
                message = f'O repositório {repository.name}, do id {repository.id} foi atualizado'
                return_list.append(message)

        for id in self.list_disabled:
            repository = self.disable_repository(id=id)
            message = f'O repositório {repository.name}, do id {repository.id} foi desativado'
            return_list.append(message)

        return self.format_response(return_list)

    def check_repositories(self):
        list_repositories = []
        for item in self.items:
            list_repositories.append(item.get('id'))
            if item.get('id') not in self.repositories:
                self.list_update.append(item.get('id'))

        for repository in self.repositories:
            if repository not in list_repositories:
                self.list_disabled.append(repository)
            else:
                self.list_update.append(repository)

    def disable_repository(self, id):
        repository = self.find_repository(id)
        repository.disable()

        return repository

    @staticmethod
    def find_repository(id):
        repository = Repositories.objects.filter(id=id).first()

        return repository

    def manage_repository(self, data):
        is_created = None
        repository = self.find_repository(data.get('id'))
        if not repository:
            repository = Repositories()
            is_created = True

        repository.id = data.get('id')
        repository.name = data.get('name')
        repository.is_private = True if data.get('private') is True else False
        repository.commits_url = data.get('commits_url').split('{')[0]
        repository.created_date = data.get('created_at')
        repository.pushed_date = data.get('pushed_at')
        repository.save()

        return True, repository, is_created
