"""
URL configuration for bikewala project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from API import views
from API.views import BikeSetViewSet

router=DefaultRouter()
router.register("API/v1/bikes",BikeSetViewSet,basename="bikes")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/bikes/',views.BikeListCreateView.as_view()),
    path("API/bikes/<int:pk>/",views.BikeRetriveUpdateDestroyView.as_view()),
    path('API/bikes/brand/',views.BrandView.as_view()),
    
]+router.urls
