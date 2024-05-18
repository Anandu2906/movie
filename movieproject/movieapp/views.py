from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from .forms import MovieForm

def index(request):
    m = movie.objects.all()#fetching the data and assigning in variable.
    context = {               #passing data to dictionary.
        'movie_list': m
    }
    return render(request,  'index.html', context)

def detail(request, movie_id):
    m = movie.objects.get(id=movie_id) #fetching the movie_id and assigning it to a variable (m).
    return render(request, 'detail.html', {'m': m})

def add_movie(request):
    if request.method == "POST":# getting each table value and assigning it to variable.
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        M = movie(name=name, desc=desc, year=year, img=img)
        M.save()
    return render(request, 'add.html')

def update(request,id):# id is passed along with request to edit that particular id.
    m = movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=m)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'm': m})

def delete(request,id):
    if request.method == 'POST':
        m = movie.objects.get(id=id)
        m.delete()
        return redirect('/')
    return render(request, 'delete.html')