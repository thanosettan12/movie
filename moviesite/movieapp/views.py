from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Movie
from .forms import Movieform


# Create your views here.
def index(request):
    movie = Movie.objects.all()

    return render(request, "index.html", {'result': movie})


def details(request, movid):
    mo = Movie.objects.get(id=movid)
    return render(request, 'detail.html', {'mo': mo})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        disc = request.POST.get('disc', )
        year = request.POST.get('year', )
        img = request.FILES.get('img', )
        movie = Movie(name=name, disc=disc, year=year, img=img)
        movie.save()
        return redirect('/')

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})
def delete(request, id):
     if request.method=="POST":
         movie = Movie.objects.get(id=id)
         movie.delete()
         return redirect('/')
     return render(request,'delete.html')