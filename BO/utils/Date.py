from datetime import date, timedelta


class Date:

    @staticmethod
    def get_today_date():
        today = date.today()

        return today

    @staticmethod
    def get_yesterday_date():
        yesterday = date.today() - timedelta(days=1)

        return yesterday

    @staticmethod
    def get_week_dates():
        today = date.today()
        weekday = today.weekday()

        first_day_week = today - timedelta(days=weekday + 1)
        last_day_week = first_day_week + timedelta(days=6)

        return first_day_week, last_day_week

    @staticmethod
    def get_last_week_dates():
        today = date.today()
        weekday = today.weekday()

        first_day_last_week = today - timedelta(days=weekday+8)
        last_day_last_week = first_day_last_week + timedelta(days=6)

        return first_day_last_week, last_day_last_week

    @staticmethod
    def get_month_dates():
        today = date.today()
        year = today.year
        month = today.month
        last_day_month = 31

        first_day_month = date(year, month, 1)

        try:
            last_day_month = date(year, month, last_day_month)
        except ValueError:
            last_day_month = date(year, month, (last_day_month - 1))

        return first_day_month, last_day_month

    @staticmethod
    def get_last_month_dates():
        today = date.today()
        last_month = today.replace(day=1) - timedelta(days=1)
        year = last_month.year
        month = last_month.month

        last_day_month = 31

        first_day_last_month = date(year, month, 1)

        try:
            last_day_last_month = date(year, month, last_day_month)
        except ValueError:
            last_day_last_month = date(year, month, (last_day_month - 1))

        return first_day_last_month, last_day_last_month

    @staticmethod
    def get_year_dates():
        today = date.today()
        year = today.year

        first_day_year = date(year, 1, 1)
        last_day_year = date(year, 12, 31)

        return first_day_year, last_day_year

    @staticmethod
    def get_last_year_dates():
        today = date.today()
        last_year = today.replace(day=1, month=1) - timedelta(days=1)
        year = last_year.year

        first_day_last_year = date(year, 1, 1)
        last_day_last_year = date(year, 12, 31)

        return first_day_last_year, last_day_last_year

    def get_dates_card_commits(self):
        today = self.get_today_date()
        yesterday = self.get_yesterday_date()
        first_day_week, last_day_week = self.get_week_dates()
        first_day_last_week, last_day_last_week = self.get_last_week_dates()
        first_day_month, last_day_month = self.get_month_dates()
        first_day_last_month, last_day_last_month = self.get_last_month_dates()
        first_day_year, last_day_year = self.get_year_dates()
        first_day_last_year, last_day_last_year = self.get_last_year_dates()

        dates = {
            'today': today,
            'yesterday': yesterday,
            'first_day_week': first_day_week,
            'last_day_week': last_day_week,
            'first_day_last_week': first_day_last_week,
            'last_day_last_week': last_day_last_week,
            'first_day_month': first_day_month,
            'last_day_month': last_day_month,
            'first_day_last_month': first_day_last_month,
            'last_day_last_month': last_day_last_month,
            'first_day_year': first_day_year,
            'last_day_year': last_day_year,
            'first_day_last_year': first_day_last_year,
            'last_day_last_year': last_day_last_year
        }

        return dates

