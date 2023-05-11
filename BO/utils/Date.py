from datetime import date, timedelta, datetime

import pytz


class Date:

    @staticmethod
    def get_local_date():
        tz = pytz.timezone('America/Sao_Paulo')
        local_dt = datetime.now(tz)
        return local_dt.date()

    def get_today_date(self):
        today = self.get_today_date()

        return today

    def get_yesterday_date(self):
        yesterday = self.get_today_date() - timedelta(days=1)

        return yesterday

    def get_week_dates(self):
        today = self.get_today_date()
        weekday = today.weekday()

        first_day_week = today - timedelta(days=weekday + 1)
        last_day_week = first_day_week + timedelta(days=6)

        return first_day_week, last_day_week

    def get_last_week_dates(self):
        today = self.get_today_date()
        weekday = today.weekday()

        first_day_last_week = today - timedelta(days=weekday+8)
        last_day_last_week = first_day_last_week + timedelta(days=6)

        return first_day_last_week, last_day_last_week

    def get_month_dates(self):
        today = self.get_today_date()
        year = today.year
        month = today.month
        last_day_month = 31

        first_day_month = date(year, month, 1)

        try:
            last_day_month = date(year, month, last_day_month)
        except ValueError:
            last_day_month = date(year, month, (last_day_month - 1))

        return first_day_month, last_day_month

    def get_last_month_dates(self):
        today = self.get_today_date()
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

    def get_year_dates(self):
        today = self.get_today_date()
        year = today.year

        first_day_year = date(year, 1, 1)
        last_day_year = date(year, 12, 31)

        return first_day_year, last_day_year

    def get_last_year_dates(self):
        today = self.get_today_date()
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
