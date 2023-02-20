from django.shortcuts import render, redirect
from guitar_shop.models import Guitar
from guitar_shop.forms import GuitarForm



def guit(request):                          #Create the view for the page "index.html"
    if request.method == "POST":
        form = GuitarForm(request.POST)
        if form.is_valid():         #If the user click on the button to submit
            form.save()
            return redirect("/listing")
    else:
        form = GuitarForm()
    return render(request, "index.html", {"form": form})

def listing(request):                          #Create the view for the page "show.html"
    guitars = Guitar.objects.all()
    return render(request, "listing.html", {"guitars": guitars})

def edit(request, id):  #The page with the form for editing the data
    guitar = Guitar.objects.get(id=id)
    form = GuitarForm(instance=guitar)
    return render(request,'edit.html', {'form':form})  

def update(request, id):    #Just to update the data from edit
    guitar = Guitar.objects.get(id=id)  
    if request.method == 'POST':    #If the user click on the button to submit
        form = GuitarForm(request.POST, instance = guitar)  
        if form.is_valid():  
            #If the form is valid, the app saves the elements of the form in the table and show the page "listing"
            form.save()  
            return redirect("/listing")  
    form = GuitarForm(instance=guitar)
    return render(request,
                'edit.html',
                {'form': form})

def destroy(request, id):                   #Create a view to destroy a guitar
    guitar = Guitar.objects.get(id=id)
    guitar.delete()
    return redirect("/listing")