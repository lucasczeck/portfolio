from django.db.models import F

from BO.core.Log import Error
from projects.models import Projects


class Project:

    def __init__(self, id=None):
        self.id = id

    def get_project(self):
        project = Projects.objects.filter(id=self.id).first()

        if not project:
            return {'status': False, 'project': None, 'msg': 'Projeto não encontrado'}
        else:
            return {'status': True, 'project': project, 'msg': ''}

    @staticmethod
    def save_project(title=None, description=None, is_finished=None, is_professional=None,
                     is_approved=None, is_published=None, project_url=None, repository=None):

        try:
            project = Projects()
            project.title = title
            project.description = description
            project.is_finished = is_finished
            project.is_professional = is_professional
            project.is_approved = is_approved
            project.is_published = is_published
            project.project_url = project_url
            project.repository_id = repository
            project.save()

            response = {'status': True, 'msg': ''}

        except Exception as e:
            Error.save_error(e)
            response = {'status': False, 'msg': 'Ocorreu um erro ao salvar o projeto'}

        return response

    def edit_project(self, title=None, description=None, is_finished=None, is_professional=None,
                     is_approved=None, is_published=None, project_url=None):

        try:
            project = Projects.objects.filter(id=self.id).first()
            project.title = title
            project.description = description
            project.is_finished = is_finished
            project.is_professional = is_professional
            project.is_approved = is_approved
            project.is_published = is_published
            project.project_url = project_url
            project.save()

            response = {'status': True, 'msg': ''}

        except Exception as e:
            Error.save_error(e)
            response = {'status': False, 'msg': 'Ocorreu um erro ao salvar o projeto'}

        return response

    @staticmethod
    def get_all_projects():
        projects = Projects.objects.active().filter(is_approved=True).values().all()

        return list(projects)

    @staticmethod
    def get_list_project():
        projects = Projects.objects.active().values('id').annotate(url=F('project_url'), name=F('title'),
                                                                   status=F('is_published'))

        return list(projects)
