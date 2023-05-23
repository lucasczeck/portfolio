import aboutme.models


class PersonalInfos:

    def __init__(self):
        self.who_am_i = self.get_who_am_i()
        self.hobbies = self.get_hobbies()

    @staticmethod
    def get_who_am_i():
        who_am_i = aboutme.models.PersonalInfos.objects.active().values_list('how_i_am', flat=True).first()

        return who_am_i

    @staticmethod
    def get_hobbies():
        hobbies = list(aboutme.models.Hobbies.objects.active().values('descriptive_name'))

        return hobbies

    def get_personal_infos(self):
        personal_infos = {
            'who_am_i': self.who_am_i,
            'hobbies': self.hobbies
        }

        return personal_infos
