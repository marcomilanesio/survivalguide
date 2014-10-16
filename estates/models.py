from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import utc


class EstateList(models.Model):
    user = models.ForeignKey(User, related_name='elists')  # a user will call this "his" lists
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
        return reverse('estates:elists:detail', kwargs={'slug': self.slug})  # namespaces / slug is argument for detail

'''
class Estate(models.Model):
    NEIGH_CHOICE = (
        ('Centre Ville', 'Centre Ville'),
        ('Banlieue', 'Banlieue')
    )
    estate_list = models.ForeignKey(EstateList, related_name='estates')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    class Meta:
        ordering = ('title', 'address')
        unique_together = ('estate_list', 'title')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Estate, self).save(*args, **kwargs)
'''
