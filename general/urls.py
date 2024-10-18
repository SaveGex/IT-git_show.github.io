from django.urls import path

from . import views

app_name = 'General'

urlpatterns = [
    path('general/page=<int:page_number>/', views.GeneralView.as_view(), name='general'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),

]