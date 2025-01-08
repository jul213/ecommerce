from django.shortcuts import render
from .forms import productForm

# Create your views here.

def principal(request):
    if request.method =="POST":
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html", {"form": form})
    else:
        form = productForm()
        return render(request, "index.html", {"form" : form})