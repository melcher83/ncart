"""ncart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import users.views.create_admin
import ncart_app.views.index
import ncart_app.views.add_project

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url (r'^add-user$', users.views.create_admin.page),
    url (r'^add-user$',users.views.create_admin.page, name='create_user'),
    url (r'^index$', ncart_app.views.index.page, name='index'),
    url (r'^add-project$', ncart_app.views.add_project.page, name='add-project'),
    url (r'^add-project$', ncart_app.views.add_project.page),
    url (r'^$', ncart_app.views.index.page),
    url(r'^project-details-(?P<pk>\d+)$',ncart_app.views.project_details.page, name="project_details")

]
