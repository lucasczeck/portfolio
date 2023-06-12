import aboutme.models


class PersonalInfos:

    def __init__(self):
        self.infos = None
        self.who_am_i = None
        self.career = None
        self.__load()

    def __get_infos(self):
        self.infos = aboutme.models.Infos.objects.active().first()

    def __get_who_am_i(self):
        self.who_am_i = self.infos.who_am_i

    def __get_career(self):
        self.career = self.infos.career

    def __load(self):
        self.__get_infos()
        self.__get_career()
        self.__get_who_am_i()

    def get_personal_infos(self):
        personal_infos = {
            'who_am_i': self.who_am_i,
            'career': self.career
        }

        return personal_infos
