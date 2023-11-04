from django.db.models import Q
from django.shortcuts import render

from .forms import RateForm
from .models import Cloth, Slide, Review, Image


# Create your views here.
def home(request):
    cloth = Cloth.objects.all()
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    slides = Slide.objects.all()
    cloth = cloth.filter(category=category) if category else cloth
    cloth = cloth.filter(brand=brand) if brand else cloth
    search = request.GET.get('search')
    cloth = cloth.filter(
        Q(title__icontains=search) | Q(price__icontains=search)) if search else cloth

    return render(request, 'home.html', {'cloth': cloth, 'slides': slides})


def cloth_detail(request, pk):
    product = Cloth.objects.get(pk=pk)
    form = RateForm(request.POST or None)
    images = Image.objects.filter(product=product)
    reviews = Review.objects.filter(product=product)
    if request.method == "POST" and form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.product = product
        instance.save()
    return render(request, 'cloth_detail.html', {'product': product, 'form': form, 'reviews': reviews,'images':images})
