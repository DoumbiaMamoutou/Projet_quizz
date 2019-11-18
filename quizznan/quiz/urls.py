from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('profil', views.profil, name='profil'),
    path('quizz', views.quizz, name='quizz'),
    path('epreuve', views.epreuve, name='epreuve'),
    path('lesson', views.lesson, name='lesson'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
]
