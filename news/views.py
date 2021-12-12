from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from . import models


class NewsListView(generic.ListView):
    model = models.News



class NewsCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.News
    fields = ('title', 'text',)
    template_name = 'attacks_demonstration/xss_form.html'

    def get_success_url(self):
        return reverse('news:list', kwargs={'pk': self.object.id})
