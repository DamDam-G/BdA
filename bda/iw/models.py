from django.db import models
from django.utils.translation import ugettext_lazy as _

class Calendar(models.Model):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(_('slug'), unique=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _('calendar')
        ordering = ['name']

class Event(models.Model):
    title = models.CharField(_('title'), max_length=100)
    start = models.DateTimeField(_('start'))
    end = models.DateTimeField(_('end'))
    is_cancelled = models.BooleanField(_('Cancelled?'), default=False, blank=True)

    calendar = models.ForeignKey(Calendar)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = _('event')
        ordering = ['start', 'end']

class msg(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    msg = models.TextField()
    date = models.DateTimeField()

class follow(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.TextField()
    firstname = models.TextField()