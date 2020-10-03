from django.shortcuts import render
from .models import ImageModel



def home(request):
    prod_sliders = ImageModel.objects.all()[0]
    return render(request, 'home.html',{'prod_sliders':prod_sliders})

