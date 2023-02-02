from django.urls import path
from . import views as apiviews
from adminapp import views as adminviews
from rest_framework_simplejwt.views import (    
    TokenRefreshView,
)

urlpatterns = [
    path('api/', apiviews.getRoutes, name="api"),
    path('api/token/', apiviews.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', apiviews.Register.as_view(), name="register"),
    path('user/', apiviews.getUser.as_view(), name="user"),
    path('application/', adminviews.UserApplication.as_view(), name="application"),
    path('getapplication/', adminviews.getUserApplication.as_view(), name="getapplication"),
    path('getapplication/<int:pk>/', adminviews.getUserApplication.as_view(), name="getapplicationid"),
    path('getapplication/<str:value>/', adminviews.getUserApplication.as_view(), name="getapplicationstatus"),
    path('changeappstatus/<str:value>/<int:pk>/', adminviews.ChangeStatus.as_view(), name="changeappstatus"),
    path('getpendingapps/', adminviews.getPendingApps.as_view(), name="getpendingapps"),
    path('dashboard/', adminviews.Dashboard.as_view(), name="filterwithdate"),
    path('download/<str:fromdate>/<str:todate>/', adminviews.DownloadReport.as_view(), name="download"),

]