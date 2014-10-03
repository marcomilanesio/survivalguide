from __future__ import absolute_import

#from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.

from braces import views

from . import models
from . import forms

class RestrictToOwnerMixin(object):
    def get_queryset(self):
        queryset = super(RestrictToOwnerMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
        

class TalkListListView(
    views.LoginRequiredMixin,
    RestrictToOwnerMixin,
    generic.ListView
):
    model = models.TalkList

        

class TalkListDetailView(
    views.LoginRequiredMixin,
    #views.PrefetchRelatedMixin,
    RestrictToOwnerMixin,
    generic.DetailView
):
    model = models.TalkList
    prefetch_related = ('talks',)
    
        
    #def get(self, request, *args, **kwargs):
    #    return HttpResponse('A talk list')


class TalkListCreateView(
    views.LoginRequiredMixin,
    views.SetHeadlineMixin,
    generic.CreateView
):
    form_class = forms.TalkListForm
    headline = 'Create'
    model = models.TalkList

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(TalkListCreateView, self).form_valid(form)


class TalkListUpdateView(
    RestrictToOwnerMixin,
    views.LoginRequiredMixin,
    views.SetHeadlineMixin,
    generic.UpdateView
):
    form_class = forms.TalkListForm
    headline = 'Update'
    model = models.TalkList
