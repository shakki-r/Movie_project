from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.

def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']

        movie = Movie(name=name, description=description, year=year, image=image)

        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method=='POST':
        form = MovieForm(request.POST or None, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=MovieForm( instance=movie)

    return render(request, 'edit.html', {'form': form, 'movie': movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')

    name=Movie.objects.get(id=id)
    return render(request,'delete.html',{'name':name})