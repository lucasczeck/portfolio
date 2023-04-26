from core.integracoes.github.models import Repositories, Commits


class Cards:

    def __init__(self, date):
        self.date = date
        self.cards_projects = None
        self.load()

    @staticmethod
    def load_percentages_projects(cards):
        for card in cards:
            total = 0
            card_dict = cards.get(card)
            for value in card_dict:
                total += card_dict.get(value).get('value')

            for statistic in card_dict:
                percentage = (card_dict.get(statistic).get('value') / total * 100) \
                    if card_dict.get(statistic).get('value') and total > 0 else 0
                card_dict[statistic]['percentage'] = f"{percentage:.2f}"

        return cards

    def load(self):
        self.cards_projects = self.get_cards_projects()

    def get_cards_projects(self):
        personal_projects = Repositories.objects.filter(is_professional=False)
        professional_projects = Repositories.objects.filter(is_professional=True)

        data_projects = {
            'personal': {
                'finalized': {'value': personal_projects.filter(is_finished=True).count()},
                'development': {'value': personal_projects.filter(is_finished=False).count()},
                'published': {'value': personal_projects.filter(is_published=True).count()}
            },
            'professional': {
                'finalized': {'value': professional_projects.filter(is_finished=True).count()},
                'development': {'value': professional_projects.filter(is_finished=False).count()},
                'published': {'value': professional_projects.filter(is_published=True).count()}
            }
        }

        cards = self.load_percentages_projects(data_projects)

        return cards

    def get_cards(self):
        cards = {
            'projects': self.cards_projects
        }

        return cards
