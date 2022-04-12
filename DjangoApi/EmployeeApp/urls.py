from django.conf.urls import url
# from django.urls import path
from django.urls.resolvers import URLPattern

from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

# urlPatterns = [
#     # url(r'^department/$' , views.departmentApi),
#     # url(r'^department/([0-9]+)$' , views.departmentApi)
# ]

urlpatterns = [
       url(r'^department/$' , views.departmentApi),
   url(r'^department/([0-9]+)$' , views.departmentApi), 

 url(r'^employee/$' , views.employeeApi),
url(r'^employee/([0-9]+)$' , views.employeeApi) ,
url(r'^savefiles/$' , views.saveFile)
] + static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)