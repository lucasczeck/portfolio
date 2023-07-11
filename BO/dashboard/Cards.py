from core.integracoes.github.models import Commits
from projects.models import Projects
from BO.utils.Date import Date


class Cards:

    def __init__(self):
        self.cards_projects = None
        self.dates = None
        self.card_commits = None
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
                card_dict[statistic]['percentage'] = float(f"{percentage:.2f}")

        return cards

    @staticmethod
    def load_percentages_commits(stats):
        today_percentage = ((stats['today'] - stats['yesterday']) / stats['yesterday']) * 100 \
            if stats['yesterday'] > 0 else 100 if stats['today'] > 0 else 0
        week_percentage = ((stats['week'] - stats['last_week']) / stats['last_week']) * 100 \
            if stats['last_week'] > 0 else 100 if stats['week'] > 0 else 0
        month_percentage = ((stats['month'] - stats['last_month']) / stats['last_month']) * 100 \
            if stats['last_month'] > 0 else 100 if stats['month'] > 0 else 0
        year_percentage = ((stats['year'] - stats['last_year']) / stats['last_year']) * 100 \
            if stats['last_year'] > 0 else 100 if stats['year'] > 0 else 0

        stats['today_percentage'] = float(f"{today_percentage:.2f}")
        stats['week_percentage'] = float(f"{week_percentage:.2f}")
        stats['month_percentage'] = float(f"{month_percentage:.2f}")
        stats['year_percentage'] = float(f"{year_percentage:.2f}")

        return stats

    def load(self):
        self.cards_projects = self.get_cards_projects()
        self.dates = Date().get_dates_card_commits()
        self.card_commits = self.get_card_commits()

    def get_cards_projects(self):
        personal_projects = Projects.objects.filter(is_professional=False)
        professional_projects = Projects.objects.filter(is_professional=True)

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

    def get_card_commits(self):
        commits = Commits.objects.all()

        data_commits = {
            'today': commits.filter(date__date=self.dates['today']).count(),
            'yesterday': commits.filter(date__date=self.dates['yesterday']).count(),
            'week': commits.filter(date__date__gte=self.dates['first_day_week'],
                                   date__date__lte=self.dates['last_day_week']).count(),
            'last_week': commits.filter(date__date__gte=self.dates['first_day_last_week'],
                                        date__date__lte=self.dates['last_day_last_week']).count(),
            'month': commits.filter(date__date__gte=self.dates['first_day_month'],
                                    date__date__lte=self.dates['last_day_month']).count(),
            'last_month': commits.filter(date__date__gte=self.dates['first_day_last_month'],
                                         date__date__lte=self.dates['last_day_last_month']).count(),
            'year': commits.filter(date__date__gte=self.dates['first_day_year'],
                                   date__date__lte=self.dates['last_day_year']).count(),
            'last_year': commits.filter(date__date__gte=self.dates['first_day_last_year'],
                                        date__date__lte=self.dates['last_day_last_year']).count(),
        }

        card = self.load_percentages_commits(data_commits)

        return card

    def get_cards(self):

        cards = {
            'projects': self.cards_projects,
            'commits': self.card_commits
        }

        return cards
