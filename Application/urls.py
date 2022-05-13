from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from Application.views import CommandViewSet



route = routers.DefaultRouter()
route.register('commands', CommandViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='Auth/login.html'), name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', auth_views.LogoutView.as_view(template_name='Auth/logout.html'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('commander', views.commander, name='commander'),

    path('commander/macon', views.macon, name='macon'),
    path('commander/plombier', views.plomblier, name='plombier'),
    path('commander/reparateur-climatiseur', views.repclim, name='repclim'),
    path('commander/coiffeur', views.coiffeur, name='coiffeur'),
    path('commander/electricien', views.electricien, name='electricien'),
    path('commander/jardinier', views.jardinier, name='jardinier'),
    path('commander/cuisinier', views.cuisinier, name='cuisinier'),
    path('commander/mecanicien', views.mecanicien, name='mecanicien'),
    path('commander/lessiveur', views.lessiveur, name='lessiveur'),
    path('commander/garde-enfant', views.gardenf, name='garde-enfant'),
    path('commander/couturier', views.couturier, name='couturier'),
    path('commander/make-up', views.makeup, name='make-up'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
