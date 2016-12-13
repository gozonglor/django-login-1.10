from django.conf.urls import url

from . import views

# ecoshop-django 2\shop\views
# app_name = 'shop' -- if you have multiple apps in one project

urlpatterns = [
    url(r'^load/$', views.load_items, name='load_items'),
    url(r'^(?P<upload_id>[0-9]+)/$', views.detail, name='detail'),
]