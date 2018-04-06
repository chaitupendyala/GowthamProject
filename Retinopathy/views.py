from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from . import models

@csrf_exempt
def enter_image(request):
    return render(request,"Retinopathy/main.html",{})

@csrf_exempt
def store_image(request):
    if request.method == "POST":
        u = models.Eye_Images(image = request.FILES['image'])
        u.save()
        return redirect("/check")
    else:
        return redirect("/check")
