from django.urls import path 
from .views import MoneyListView, MoneyUpdateView, MoneyDeleteView, MoneyCreateView

urlpatterns = [
    path('', MoneyListView.as_view(), name = 'list_view'),
    path('<int:pk>/update/', MoneyUpdateView.as_view(), name = 'update_view'),
    path('create/', MoneyCreateView.as_view(), name = 'create_view'),
    path('<int:pk>/delete/', MoneyDeleteView.as_view(), name = 'delete_view'),
]