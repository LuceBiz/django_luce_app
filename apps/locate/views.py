from unicodedata import name
from django.shortcuts import render, redirect
from requests import request
from .models import Category, Info, Coupon
from .forms import CouponCreateForm, CouponSearchForm, CouponUpdateForm
from django.contrib.auth.decorators import login_required
import folium

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


def addLocation(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        print('data:', data)
        print('image:', image)

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        info = Info.objects.create(
            category = category,
            description = data['description'],
            image = image,
        )

        return redirect('state')

    context = {
        'categories' : categories,
        }
    return render(request, 'locate/add.html', context)

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

def add_items(request):
    form = CouponCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_items')

    context = {
        'form' : form,
        'title' : 'Add Item',
    }
    return render(request, 'locate/add_items.html', context)


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

