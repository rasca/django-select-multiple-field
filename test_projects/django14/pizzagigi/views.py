# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView

from .models import Pizza


class PizzaListView(ListView):

    queryset = Pizza.objects.order_by('-id')
    context_object_name = 'pizzas'
    paginate_by = 10


class PizzaCreateView(CreateView):

    model = Pizza
    success_url = reverse_lazy('pizza:created')


class PizzaDetailView(DetailView):

    model = Pizza


class PizzaUpdateView(UpdateView):

    model = Pizza
    success_url = reverse_lazy('pizza:updated')

class PizzaDeleteView(DeleteView):

    model = Pizza
    success_url = reverse_lazy('pizza:deleted')