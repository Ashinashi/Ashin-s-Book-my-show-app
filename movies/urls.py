from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('process-payment/', views.process_payment, name='payment_process'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('favorite/<int:movie_id>/', views.favorite_movie, name='favorite_movie'),
    path('payment/', views.payment, name='payment'),
    path('process-payment/', views.process_payment, name='payment_process'),
    path('theatres/', views.theatres, name='theatres'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('like/<int:movie_id>/', views.like_movie, name='like_movie'),
    path('favorites/', views.favorites, name='favorites'),
    path('theatres/', views.theatres, name='theatres'),
    path('releases/', views.releases, name='releases'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
