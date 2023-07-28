from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('save/',views.save_contact,name='save'),
    path('delete/',views.delete_contact,name='delete'),
    path('edit/',views.edit_contact,name='edit'),
    path('data/',views.data,name='data'),

]