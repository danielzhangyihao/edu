from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^courses/', views.index, name='courseHome'),
	url(r'^get_courses/', views.get_courses, name='getCourses'),
]