from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    peoples=[
        {'name':'abhishek','age':26},
        {'name':'abhi','age':26},
        {'name':'shek','age':26},
        {'name':'bhish','age':26},
        {'name':'ish','age':26},

    ]
    return render(request,"index.html", context={'peoples':peoples} )

def success_page(requst):
    # print("*" *10)
    return HttpResponse("<h1>this is second page</h1>")