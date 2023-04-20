from django.db import models
from django.utils import timezone


class DatLog(models.Model):
    dat_insercao = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dat_edicao = models.DateTimeField(auto_now=True, null=True, blank=True)
    dat_delete = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        abstract = True


class Log(DatLog):
    normal_objects = models.Manager()

    status = models.BooleanField(null=True, default=True)

    class Meta:
        managed = True
        abstract = True

    def save(self, request_=None, *args, **kwargs):
        if self.dat_insercao is None:
            self.dat_insercao = timezone.now()
            self.status = True
        else:
            self.dat_edicao = timezone.now()

        super(Log, self).save(*args, **kwargs)
