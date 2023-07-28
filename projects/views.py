from django.http import JsonResponse
from rest_framework.views import APIView

from BO.projects.Repository import Repository
from BO.projects.Project import Project


class GetRepositoriesView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        repositories = Repository.get_pending_repositories()

        return JsonResponse(repositories, safe=False)


class GetProjectsView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        projects = Project.get_all_projects()

        return JsonResponse(projects, safe=False)


class ProjectView(APIView):

    def get(self, *args, **kwargs):
        project_id = self.request.GET.get('project_id')

        project = Project(id=project_id).get_project()

        return JsonResponse(project, safe=False)

    def post(self, *args, **kwargs):
        project_id = self.request.POST.get('project_id')
        repository_id = self.request.POST.get('repository_id')
        title = self.request.POST.get('title')
        description = self.request.POST.get('description')
        is_finished = self.request.POST.get('is_finished')
        is_professional = self.request.POST.get('is_professional')
        is_approved = self.request.POST.get('is_approved')
        is_published = self.request.POST.get('is_published')
        project_url = self.request.POST.get('project_url')

        parametros = {'title': title, 'description': description, 'is_finished': is_finished,
                      'is_professional': is_professional, 'is_approved': is_approved, 'is_published': is_published,
                      'project_url': project_url}

        project = Project(id=project_id)

        if project_id:
            response = project.edit_project(**parametros)
        else:
            response = project.save_project(**parametros, repository=repository_id)

        return JsonResponse(response, safe=False)
