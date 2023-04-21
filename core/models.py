from django.db import models
from django.utils import timezone


class InteligerQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=True)

    def disable(self):
        qs = self.update(status=False, dat_delete=timezone.now())
        return qs


class InteligerManager(models.Manager):
    def queryset(self):
        return InteligerQuerySet(self.model)

    def get_queryset(self):
        qs = self.queryset()

        return qs

    def active(self):
        return self.get_queryset().active()

    def disable(self):
        return self.get_queryset().disable()


class DatLog(models.Model):
    dat_insercao = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dat_edicao = models.DateTimeField(auto_now=True, null=True, blank=True)
    dat_delete = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        abstract = True


class Log(DatLog):
    normal_objects = models.Manager()
    objects = InteligerManager()

    status = models.BooleanField(null=True, default=True)

    class Meta:
        managed = True
        abstract = True

    def save(self, *args, **kwargs):
        if self.dat_insercao is None:
            self.dat_insercao = timezone.now()
            self.status = True
        else:
            self.dat_edicao = timezone.now()

        super(Log, self).save(*args, **kwargs)

    def disable(self, *args, **kwargs):
        self.status = False
        self.dat_delete = timezone.now()
        super(Log, self).save(*args, **kwargs)
