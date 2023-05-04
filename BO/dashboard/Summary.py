from dashboard.models import HardSkills, SoftSkill, Personal, Experience


class Summary:

    def __init__(self):
        self.personal_infos = None
        self.parents_hard_skills = None
        self.parents_soft_skills = None
        self.load()

    def load(self):
        self.parents_hard_skills = list(HardSkills.objects.filter(parent_skill__isnull=True))
        self.parents_soft_skills = list(SoftSkill.objects.filter(parent_skill__isnull=True))
        self.personal_infos = Personal.objects.first()

    def load_hardskills(self):
        list_hardskills = []
        for parent_skill in self.parents_hard_skills:
            skills = list(HardSkills.objects.filter(parent_skill=parent_skill.pk)
                          .values('descriptive_name', 'description'))
            a = {parent_skill.descriptive_name: {'description': parent_skill.description, 'skills': skills}}

            list_hardskills.append(a)

        return list_hardskills

    def load_softskills(self):
        list_softskills = []
        for parent_skill in self.parents_soft_skills:
            skills = list(SoftSkill.objects.filter(parent_skill=parent_skill.pk)
                          .values('descriptive_name', 'description'))
            a = {parent_skill.descriptive_name: {'description': parent_skill.description, 'skills': skills}}

            list_softskills.append(a)

        return list_softskills

    def load_last_experience(self):
        experience = Experience.objects.filter(id=self.personal_infos.last_experience_id)\
            .values('company', 'started', 'end', 'position', 'description').first()

        return experience

    def get_summary(self):
        summary = {
            'photo': self.personal_infos.photo,
            'title': self.personal_infos.title,
            'hardskills': self.load_hardskills(),
            'softskills': self.load_softskills(),
            'last_experience': self.load_last_experience()
        }

        return summary
