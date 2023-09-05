from core.admin.models import Module, Cards
from django.template import Template, Context

from core.integracoes.github.models import Repositories


class CardsAdmin:

    @staticmethod
    def get_modulos():
        modules = list(Module.objects.active().values('name'))

        return modules

    def get_cards(self):
        cards = list(Cards.objects.active().filter(module__status=True)
                     .values('title', 'description', 'access', 'url', 'module__name'))

        for card in cards:
            context = self.get_amount_card(module=card['module__name'])
            if context.get('amount'):
                card['amount'] = context['amount']
            card['description'] = self.process_infos(context=context, conteudo=card['description'])

        return cards

    @staticmethod
    def process_infos(context=None, conteudo=None):
        t = Template(conteudo)
        c = Context(context)
        result = t.render(c)

        return result

    def get_amount_card(self, module=None):
        if module is None:
            return '0'

        elif module == 'projects':
            return self.get_amount_projects()

    @staticmethod
    def get_amount_projects():
        amount = Repositories.objects.active().exclude(is_project_created=True).count()

        return {'amount': amount}
