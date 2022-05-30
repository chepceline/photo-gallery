from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos':photos}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


def search_image(request):
    title = 'Search'
    return render(request, 'search.html')


 
