from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import MyModel
from django.urls import reverse_lazy, reverse

# Create your views here.

class MoneyListView(ListView):
    model = MyModel 
    template_name = 'list_view.html'

class MoneyUpdateView(UpdateView):
    model = MyModel 
    fields = ('money_take','money_give',)
    template_name = 'update_View.html'
    success_url = reverse_lazy('list_view')

class MoneyDeleteView(DeleteView):
    model = MyModel 
    template_name = 'delete_view.html'
    success_url = reverse_lazy('list_view')

class MoneyCreateView(CreateView):
    model =  MyModel 
    template_name = 'create_view.html'
    fields = ('name', 'email', 'money_take', 'money_give',)
    success_url = reverse_lazy('list_view')


