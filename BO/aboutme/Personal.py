import aboutme.models


class PersonalInfos:

    def __init__(self):
        self.who_am_i = self.__get_who_am_i()

    @staticmethod
    def __get_who_am_i():
        who_am_i = aboutme.models.Infos.objects.active().values_list('who_am_i', flat=True).first()

        return who_am_i

    def get_personal_infos(self):
        personal_infos = {
            'who_am_i': self.who_am_i,
        }

        return personal_infos
