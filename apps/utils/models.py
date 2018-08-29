from django.db import models
from apps.third_party_apps.fcm.models import Device
from .apps import APP_NAME
from apps.utils import shortcuts as objects_
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class BaseAppModel(models.Model):
    APP_NAME = APP_NAME

    class Meta:
        abstract = True


class HotelGranMaleconQueryset(models.QuerySet):

    def archive(self):
        return self.filter(archive=True)

    def all_unarchived(self):
        return self.filter(archive=False)


class HotelGranMaleconModelManager(BaseUserManager):
    def get_queryset(self):
        return HotelGranMaleconQueryset(self.model, using=self._db)

    def archive(self):
        return self.get_queryset().archive().order_by('-id')

    def all_unarchived(self):
        return self.get_queryset().all_unarchived().order_by('-id')


class BaseHotelGranMaleconModel(BaseAppModel):
    model_prefix = 'model'
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    archive = models.BooleanField(default=False, editable=False)
    objects = HotelGranMaleconModelManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def mark_as_archive(self):
        self.archive = True
        self.save()

    def get_kwargs(self):
        return {
            'pk': self.pk
        }

    def get_base_url(self, action):
        return reverse_lazy('{}:{}_{}'.format(
            self.APP_NAME, action, self.model_prefix
        ), kwargs=self.get_kwargs())

    def get_absolute_url(self):
        return self.get_base_url('detail')

    def get_update_url(self):
        return self.get_base_url('update')

    def get_archive_url(self):
        return self.get_base_url('archive')

    @classmethod
    def get_create_url(cls):
        return reverse_lazy('{}:create_{}'.format(
            cls.APP_NAME,
            cls.model_prefix
        ))

    @classmethod
    def get_list_url(cls):
        return reverse_lazy('{}:list_{}'.format(
            cls.APP_NAME,
            cls.model_prefix
        ))

    def get_time(self, time):
        return time.strftime("%I:%M %p")

    def get_date(self, date):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        return date.strftime('%d de %B de %Y')


class PushNotification(object):

    titulo = None
    motivo = None

    def send_push_notification(self, titulo, motivo):
    	self.titulo = titulo
    	self.motivo = motivo
        for device in Device.objects.all():
            device.send_message(self.get_notification_data())

    def get_notification_data(self):
        return {
            "notification": {
                "title": "{}".format(self.titulo),
                "body": "{}".format(self.motivo)
            }
        }