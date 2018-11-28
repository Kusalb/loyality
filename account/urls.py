from django.template.context_processors import static
from django.urls import path

from loyality import settings
from . import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),

    url(r'^partner/$', views.partner_list, name='partner_list'),
    url(r'^partner/(?P<pk>[0-9]+)/$', views.partner_detail, name='partner_detail'),
    url(r'^partner/new/$', views.partner_new, name='partner_new'),
    url(r'^partner/(?P<pk>[0-9]+)/edit/$', views.partner_edit, name='partner_edit'),
    url(r'^partner/(?P<pk>[0-9]+)/delete/$', views.partner_delete, name='partner_delete'),


    url(r'^waiter/$', views.waiter_list, name='waiter_list'),
    url(r'^waiter/new/$', views.waiter_new, name='waiter_new'),
    url(r'^waiter/(?P<pk>[0-9]+)/edit/$', views.waiter_edit, name='waiter_edit'),
    url(r'^waiter/(?P<pk>[0-9]+)/delete/$', views.waiter_delete, name='waiter_delete'),

    url(r'^promotion/$', views.promotion_list, name='promotion_list'),
    url(r'^promotion/new/$', views.promotion_new, name='promotion_new'),
    url(r'^promotion/(?P<pk>[0-9]+)/edit/$', views.promotion_edit, name='promotion_edit'),
    url(r'^promotion/(?P<pk>[0-9]+)/delete/$', views.promotion_delete, name='promotion_delete'),




]