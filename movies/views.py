from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect
from .models import Movie

# movies/views.py
from django.shortcuts import render


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # this enables /accounts/login/
]

def payment(request):
    amount = request.GET.get('amount', 0)
    return render(request, 'movies/payment.html', {'amount': amount})


def favorite_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.favorite = not movie.favorite
    movie.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def home(request):
    slider_movies = Movie.objects.all()[:5]
    top_movies = Movie.objects.all()[:10]

    context = {
        'slider_movies': slider_movies,
        'top_movies': top_movies,
    }
    return render(request, 'movies/home.html', context)

@login_required
def favorites(request):
    fav_movies = request.user.profile.liked_movies.all()
    return render(request, 'movies/favorites.html', {'fav_movies': fav_movies})

@login_required
def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    profile = request.user.profile

    if movie in profile.liked_movies.all():
        profile.liked_movies.remove(movie)
    else:
        profile.liked_movies.add(movie)

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def favorite_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.favorite = not movie.favorite
    movie.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def movies(request):
    all_movies = Movie.objects.all()
    liked = []
    if request.user.is_authenticated:
        liked = request.user.profile.liked_movies.all()

    for movie in all_movies:
        movie.liked = movie in liked

    return render(request, 'movies/movies.html', {'movies': all_movies})

def theatres(request):
    return render(request, 'movies/theatres.html')

def releases(request):
    return render(request, 'movies/releases.html')
def payment(request):
    return render(request, 'movies/payment.html')
def payment(request):
    amount = request.GET.get('amount', 0)
    return render(request, 'movies/payment.html', {'amount': amount})
def releases(request):
    top_movies = Movie.objects.all()[:6]
    return render(request, 'movies/releases.html', {'top_movies': top_movies})
def releases(request):
    slider_movies = Movie.objects.all()[:5]  # or any number of top movies
    return render(request, 'movies/releases.html', {
        'slider_movies': slider_movies
    })

def process_payment(request):
    amount = request.GET.get('amount')
    # Handle payment logic here
    return render(request, 'movies/payment_success.html', {'amount': amount})

from django.contrib.auth.views import LoginView

class MyLoginView(LoginView):
    template_name = 'movies/my_login.html'  # or wherever your custom login template is
