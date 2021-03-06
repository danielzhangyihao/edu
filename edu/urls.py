"""edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views import generic
from user import views as user_views

urlpatterns = [
	url(r'^user/', include('user.urls')),
    url(r'^education/', include('education.urls')),
	url(r'^signup/', user_views.register, name='signup'),
    url(r'^signout/', user_views.signout, name='signout'),
    url(r'^login/', user_views.signin, name='login'),
    url(r'^activate/', user_views.activate, name='activate'),
    url(r'^admin/', admin.site.urls),
    url(r'^$',
        generic.TemplateView.as_view(template_name='landing.html')),
    url(r'^home/',
        generic.TemplateView.as_view(template_name='index.html')),
    url(r'^about/',
        generic.TemplateView.as_view(template_name='about.html')),   
    url(r'^course/',
        generic.TemplateView.as_view(template_name='course_page.html')),   
    url(r'^settings/',
        generic.TemplateView.as_view(template_name='settings.html')),   
    url(r'^update_password/',
        user_views.update_password, name='update_password'),
    url(r'^update_firstName/',
        user_views.update_firstName, name='update_firstName'),
    url(r'^update_lastName/',
        user_views.update_lastName, name='update_lastName'),
    url(r'^education/', include('education.urls')),
]
