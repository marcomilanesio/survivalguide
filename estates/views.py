from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from django.views import generic

from braces import views

from . import models
from . import forms

class RestrictToUserMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(RestrictToOwnerMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class EstateListListView(
    RestrictToUserMixin,
    generic.ListView
):
    model = models.EstateList

    def get_queryset(self):
        return self.request.user.elists.all()
        

class EstateListDetailView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('An Estate list')


class EstateListDetailView(
    views.LoginRequiredMixin,
    #RestrictToUserMixin,
    #views.PrefetchRelatedMixin,
    generic.DetailView
):
    #form_class = forms.EstateForm
    #http_method_names = ['get', 'post']
    model = models.EstateList
    prefetch_related = ('estates',)

    def get_context_data(self, **kwargs):
        context = super(EstateListDetailView, self).get_context_data(**kwargs)
        context.update({'form': self.form_class(self.request.POST or None)})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = self.get_object()
            estate = form.save(commit=False)
            estate.estate_list = obj
            estate.save()
        else:
            return self.get(request, *args, **kwargs)
        return redirect(obj)

            
    def get_queryset(self):
        queryset = super(EstateListDetailView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class EstateListCreateView(
    views.LoginRequiredMixin,
    views.SetHeadlineMixin,
    generic.CreateView
):
    form_class = forms.EstateListForm
    headline = 'Create'
    model = models.EstateList

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(EstateListCreateView, self).form_valid(form)


class EstateListUpdateView(
    #RestrictToOwnerMixin,
    views.LoginRequiredMixin,
    views.SetHeadlineMixin,
    generic.UpdateView
):
    form_class = forms.EstateListForm
    headline = 'Update'
    model = models.EstateList
