from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from . import models


class NewsListView(generic.ListView):
    model = models.News


class NewsCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.News
    fields = ('title', 'text',)

    def form_valid(self, form):
        self.object: models.News = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('news:list')
