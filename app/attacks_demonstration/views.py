from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from . import models


def index(request):
    return render(request, 'attacks_demonstration/index.html')

class XssCreateView(generic.CreateView):
    model = models.TestData
    fields = ('text',)
    template_name = 'attacks_demonstration/xss_form.html'

    def get_success_url(self):
        return reverse('attacks_demonstration:xss_detail', kwargs={'pk': self.object.id})


class XssDetailView(generic.DetailView):
    model = models.TestData
    fields = ('text',)
    template_name = 'attacks_demonstration/xss_detail.html'
