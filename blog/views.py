from django.http import Http404
from django.shortcuts import render
from .models import Products, Client, Video, Remot

# Create your views here.
def index(request):
    product = Products.objects.all()
    video = Video.objects.all()
    client = Client.objects.all()
    context = {
        "product": product,
        "video": video,
        "client": client,
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, "about.html", context={})

def contact(request):
    return render(request, "contact.html", context={})


def product(request):
    video = Video.objects.all()
    remot = Remot.objects.all()
    context = {
        "video": video,
        "remot": remot
    }
    return render(request, "product.html", context=context)

def productdetailview(request, id):
    try:
        product = Products.objects.get(id=id)
        context = {
            "product": product
            }
    except product.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "product_detail.html", context=context)


def remot(request):
    remot = Remot.objects.all()
    context = {
        "remot": remot
    }
    return render(request, "remot.html", context=context)

def video(request):
    video = Video.objects.all()
    context = {
        "video": video
    }
    return render(request, "video.html", context=context)

def videodetailview(request, id):
    try:
        video = Video.objects.get(id=id)
        context = {
            "video":video
        }
    except video.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "video_detail.html", context=context)


def contactdetailview(request, id):
    try:
        contact = Client.objects.get(id=id)
        context = {
            "contact": contact
        }
    except contact.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "contact_detail.html", context=context)

def remotdetailview(request, id):
    try:
        remot = Remot.objects.get(id=id)
        context = {
            "remot": remot
        }
    except contact.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "remot_detail.html", context=context)

