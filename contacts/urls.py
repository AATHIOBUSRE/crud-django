from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.contact_form,name='contact_insert'), #get and post req for insert
    path('<int:id>/',views.contact_form,name='contact_update'),  #get and post req for update
    path('delete/<int:id>/',views.contact_delete,name='contact_delete'),
    path('list/',views.contact_list,name='contact_list')  #get req to retrive and display all records
]