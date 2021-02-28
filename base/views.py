from django.shortcuts import render, HttpResponse
from .models import * # we can use (from appname.models import * )also

# Create your views here.
def home(request):
    images = Image.objects.all()
    category = Category.objects.all()
    data = {"images": images, "category": category}
    return render(request, 'home.html', data)


def aboutus(request):
    return HttpResponse("Hello About page!!")

def show_category(request, cid):
    
    ## it will show all category
    category = Category.objects.all()

    ## it will return only selected category
    cat = Category.objects.get(pk = cid)

    images = Image.objects.filter(cat = cat)
    data = {'images': images, 'category': category}
    
    return render(request, 'home.html', data)


    