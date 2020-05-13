from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path("<slug:category_url>/", views.ServiceListView.as_view(), name='service_list'),
    path("/<slug:slug>/", views.ServiceDetailView.as_view(), name='service_detail')
]