from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Eye_Images
import subprocess
import os

def enter_image(request):
    return render(request,"Retinopathy/main.html",{})

@csrf_exempt
def store_image(request):
    if request.method == "POST":
        u = Eye_Images(image = request.FILES['image'])
        u.save()
        return_val = evaluate(u.id)
        vals = return_val.split(" ")
        print vals
        return HttpResponse("<h1>Class 1 resemblence is :"+str(float(vals[1])*100)+"<br/>"+"Class 2 resemblence is :"+str(float(vals[3].split("]")[0])*100))
    else:
        return redirect("/check")

def evaluate(id_of_object):
    process = subprocess.Popen(['python', os.getcwd()+'/Retinopathy/trur_eval.py', str(Eye_Images.objects.get(id = id_of_object).image.path)], stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out
