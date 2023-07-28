import os

from core.models import LogError


class Error:

    @staticmethod
    def save_error(exception):
        line = exception.__traceback__.tb_lineno
        nm_function = exception.__traceback__.tb_frame.f_code.co_name
        nm_file = os.path.relpath(exception.__traceback__.tb_frame.f_globals['__file__'])
        nm_class = exception.__traceback__.tb_frame.f_globals['__name__']
        message = str(exception)

        LogError(line=line, nm_function=nm_function, message=message, nm_file=nm_file, nm_class=nm_class).save()
