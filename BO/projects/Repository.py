from core.integracoes.github.models import Repositories


class Repository:

    @staticmethod
    def get_pending_repositories():
        repositories = Repositories.objects.active().filter(is_project_created=False).values().all()

        return list(repositories)
