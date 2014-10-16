from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify  # check others for unicode

class TalkList(models.Model):
    user = models.ForeignKey(User, related_name='lists')  # a user will call this "his" lists
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)    

    class Meta:
        unique_together = ('user', 'name')  # you cannot have more than 1 list with your name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TalkList, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('talks:lists:detail', kwargs={'slug': self.slug})  # namespaces / slug is argument for detail


class Talk(models.Model):
    ROOM_CHOICES = (
        ('517D', '517D'),
        ('517C', '517C'),
        ('517AB', '517AB'),
    )
    talk_list = models.ForeignKey(TalkList, related_name='talks')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    when = models.DateTimeField()
    room = models.CharField(max_length=5, choices=ROOM_CHOICES)
    host = models.CharField(max_length=255)
    talk_rating = models.IntegerField(blank=True, default=0)
    speaker_rating = models.IntegerField(blank=True, default=0)

    @property
    def overall_rating(self):
        if self.talk_rating and self.speaker_rating:
            return (self.talk_rating + self.speaker_rating) / 2
        return 0
     
    class Meta:
        ordering = ('when', 'room')
        unique_together = ('talk_list', 'name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Talk, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('talks:talks:detail', kwargs={'slug': self.slug})
