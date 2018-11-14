
from django.contrib import admin
from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




from rest_framework.urlpatterns import format_suffix_patterns
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waiters/', views.WaiterList.as_view(), name='users'),
    path('offers/', views.offerList.as_view(), name='offer'),
    path('partners/', views.PartnerList.as_view(), name='Partner'),
    path('promotions/', views.PromotionList.as_view(), name='Promotion'),
    path('transactions/', views.PartnerList.as_view(), name='Trasaction'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),





]

urlpatterns = format_suffix_patterns(urlpatterns)
