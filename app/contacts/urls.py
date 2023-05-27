from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index , name='index'),
    path('<int:pk>/', views.contact_details , name='contact_details'),
    path('add/', views.ContactNumberCreate.as_view() , name='add_contact'),
]
