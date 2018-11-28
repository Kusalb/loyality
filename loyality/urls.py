
from django.contrib import admin
from django.urls import path , include
from django.conf.urls import url

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from django.views.generic.base import TemplateView


from rest_framework.urlpatterns import format_suffix_patterns
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waiters/', views.WaiterList.as_view(), name='users'),
    path('offers/', views.offerList.as_view(), name='offer'),
    path('partners/', views.PartnerList.as_view(), name='Partner'),
    path('promotions/', views.PromotionList.as_view(), name='Promotion'),
    path('transactions/', views.PartnerList.as_view(), name='Trasaction'),
    path('discount/', views.DiscountList.as_view()),
    path('customer/', views.CustomerList.as_view()),
    path('userid/', views.UserIdList.as_view()),

    url(r'^partner/', include('account.urls')),
    url(r'^waiter/', include('account.urls')),
    url(r'^promotion/', include('account.urls')),




    # path('login/', views.LoginView, name='login'),




    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),



    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('account.urls')),
    path('users/', include('django.contrib.auth.urls')),
]




urlpatterns = format_suffix_patterns(urlpatterns)
