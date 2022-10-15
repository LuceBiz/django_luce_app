from unicodedata import name
from django.shortcuts import render, redirect
from requests import request
from .models import Category, Info, Coupon, Film
from .forms import CouponCreateForm, CouponSearchForm, CouponUpdateForm
from django.contrib.auth.decorators import login_required
import folium
from taggit.models import Tag
from rest_framework.generics import ListAPIView
from .serializers import FilmSerializer

#####HOME#######
def state(request):
    return render(request, 'locate/state.html')


def viewState(request):
    category = request.GET.get('category')

    if category == None:
        infos = Info.objects.all()
    else:
        infos = Info.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'infos' : infos,
        }
    
    print(infos)
    return render(request, 'locate/grid.html', context)

def infoLocation(request, pk):
    info = Info.objects.get(id=pk)
    stuff = Info.objects.all()
    io = info.id - 2
    cu = Info.objects.get(name=stuff[io])

    g = cu.latitude
    p = cu.longitude

    if (g==None) and (p == None):
        m = ''
    else:
        m = folium.Map(location=[g, p], zoom_start=7)
        folium.Marker(location=[g, p]).add_to(m)
        m = m._repr_html_()

    context = {
        'info':info,
        'm' : m,
        'stuff':stuff
    }

    return render(request, 'locate/location_info.html', context)

######NEW#####

@login_required
def list_items(request):
    title = 'List of items'
    queryset = Coupon.objects.all()
    form = CouponSearchForm(request.POST or None)
    if request.method == 'POST':
        queryset = Coupon.objects.filter(
        shop__icontains=form['shop'].value(),
        coupon_type=form['coupon_type'].value()
        )
    
    context = {
        'title' : title,
        'form' : form,
        'queryset' : queryset,
    }

    return render(request, 'locate/list_items.html', context)

def update_items(request, pk):
    queryset = Coupon.objects.get(id=pk)
    form = CouponUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = CouponUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_items')
    context = {
        'form' : form
    }

    return render(request, 'locate/add_items.html', context)


def delete_items(request, pk):
    queryset = Coupon.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_items')
    
    return render(request, 'locate/delete_items.html')

######COMMODITY#####

def index(request):
    films = Film.objects.prefetch_related('tags').all()
    tags = Tag.objects.all()

    context = {
        'films' : films,
        'tags' : tags
    }
    return render(request, 'locate/stuff.html', context)

class FilmListAPIView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


