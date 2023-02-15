from django.shortcuts import render, redirect
from crud_app.models import Items
from crud_app.forms import ArtcileFrom 

# Create your views here.

def home(request):
    itemslar = Items.objects.all()
    form = ArtcileFrom(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect("home")
    form = ArtcileFrom()
    return render (request, "home.html",{"items":itemslar,"form":form})


def article_delete(request, id):
    student = Items.objects.get(id=id).delete()
    return redirect('home') 

def shop_edit(request, id):
    items = Items.objects.get(id=id)
    form = ArtcileFrom(request.POST or None, instance=items)
    if form.is_valid():
        form.save()
        return redirect('home.html')
    return render(request, 'shop_edit.html',{"form":form})  


    


