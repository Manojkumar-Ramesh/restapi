"""
URL configuration for musiczone project.

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
router=DefaultRouter()

from api import views
from api.views import MovieViewsetView
router.register("api/v1/movies",MovieViewsetView,basename="movies")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/',views.HellowworldView.as_view()),
    path('morning/',views.MorningView.as_view()),
    path('addition/',views.AdditionView.as_view()),
    path('division/',views.DivisionView.as_view()),
    path('bmi/',views.BmiView.as_view()),
    path('calorie/',views.CalorieView.as_view()),
    path('emi/',views.EmiView.as_view()),
    path('api/movie/',views.MovieView.as_view()),
    path('api/movies/',views.MovieListCreateView.as_view()), 
    path('api/movies/<int:pk>/',views.MovieRetriveUpdateDestroyView.as_view()), 
    path('api/movies/genre/',views.MovieGenre.as_view()),
    path('api/movies/language/',views.MovieLanguage.as_view()),

]+router.urls
