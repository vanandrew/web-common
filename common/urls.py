from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('index', views.index_page, name='index'),
    path('lab_members', views.people_page, name='people'),
    path('research', views.research_page, name='research'),
    path('publications', views.publications_page, name='publications'),
    path('news', views.news_page, name='news'),
    path('data', views.data_page, name='data'),
    path('software', views.software_page, name='software'),
    path('directions', views.directions_page, name='directions'),
    path('participate', views.participate_page, name='participate'),
    path('careers', views.careers_page, name='careers'),
    path('contact', views.contact_page, name='contact'),
]
