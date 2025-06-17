from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def receipes(request):
    if request.method=="POST":
        data=request.POST

        receipe_image=request.FILES.get('receipe_image')
        receipe_name= data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        
        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )



        # print(receipe_description)
        # print(receipe_name)
        # print(receipe_image)


        return redirect('/receipe/')
    queryset=Receipe.objects.all()
    context={'receipes':queryset}
    return render(request, 'receipe.html')

def delete_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    
    return redirect('/receipes/')

# return render(request, 'receipes.html')

    # print(id)
