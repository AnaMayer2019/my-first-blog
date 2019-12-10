from django.shortcuts import render, get_object_or_404
from .models import Items, Category

def index(request):
    items = Items.objects.all()
    category = Category.objects.all()
    return render(request, 'shop/index.html', {'items':items, 'category':category})

def about(request):
    return render(request, 'shop/about.html', {})

def category_list(request, pk):
    c = get_object_or_404(Category, pk=pk)
    return render(request, 'shop/category.html', {'c': c})