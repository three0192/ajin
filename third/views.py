from django.shortcuts import render
from third.models import Restaurant

from third.forms import RestaurantForm
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404

def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)
    
    page = request.GET.get('page')
    items = paginator.get_page(page)
    
    print("==========================")

    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)

def detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    
    context = {
        'restaurant' :restaurant
    
    }
    
    return render(request, 'third/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return HttpResponseRedirect('/thrid/list/')
        form = RestaurantForm()
        return render(request, 'third/create.html',{form : form} )
    
def delete(request,id):
    item = get_object_or_404(Restaurant, pk=id)
    item.delete()
    return HttpResponseRedirect('/third/list/')

def update(request):
    
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        form = RestaurantForm(request.POST,  instance=item)
        if form.is_valid():
            item = form.save()
    elif 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html',{'form':form})
    return HttpResponseRedirect('/third/list/')