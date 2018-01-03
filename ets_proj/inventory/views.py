from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from . import models

class IndexView(TemplateView):
    template_name = 'inventory/index.html'

class DashboardListView(ListView):
    context_object_name = 'equipment'
    model = models.Equipment
    template_name = 'inventory/index_admin.html'

class EquipmentListView(ListView):
    context_object_name = 'equipment'
    model = models.Equipment

class EquipmentDetailView(DetailView):
    context_object_name = 'equipment'
    model = models.Equipment
    template_name = 'inventory/equipment_list_detail.html'
