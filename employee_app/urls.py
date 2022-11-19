from django.urls import URLPattern, path
from employee_app import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('view',views.view_employee,name='view_employee'),
    path('add',views.add_employee,name='add_employee'),
    path('remove',views.remove_employee,name='remove_employee'),
    path('filter',views.filter_employee,name='filter_employee')
]
