from contact.models import ContactInfo


class Info:

    @staticmethod
    def get_contact_infos():
        contact_infos = ContactInfo.objects.active().first()

        return {'status': True if contact_infos else False, 'infos': contact_infos,
                'msg': '' if contact_infos else 'Erro ao buscar informações de contato'}
