from django.shortcuts import render, redirect
from .models import Category, Photo, Location
from django.http  import HttpResponse, Http404
# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.get_all_images()
    locations = Location.objects.all()
    title = 'Gallery'

    return render(request, 'photos/gallery.html',{ 'images':photos, 'locations':locations})
    
# def viewPhoto(request, pk):
#     photo = Photo.objects.get(id=pk)
#     return render(request, 'photos/photo.html', {'photo': photo})


def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Photo.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'photos/search.html',{"message": message})



def location_filter(request, image_location):
    locations = Location.objects.all()
    location = Location.get_location_id(image_location)
    images = Photo.filter_by_location(image_location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations, 'location':location})

      


    
    r

 
