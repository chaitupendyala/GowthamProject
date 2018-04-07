from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Eye_Images
import cv2
import numpy as np
import keras
from keras.models import load_model

model = load_model("G:\DR_Two_Classes_recall_0.7759.h5")

def enter_image(request):
    return render(request,"Retinopathy/main.html",{})

@csrf_exempt
def store_image(request):
    if request.method == "POST":
        u = Eye_Images(image = request.FILES['image'])
        u.save()
        return_val = evaluate(u.id)
        return HttpResponse("<h1>Class 1 resemblence is :"+return_val[0]+"<br/>"+"Class 2 resemblence is :"+return_val[1])
    else:
        return redirect("/check")

def evaluate(id_of_object):
    image_path = str(Eye_Images.objects.get(id = id_of_object).image.path)
    image = cv2.imread(image_path)
    image = cv2.resize(image,(256,256))
    image = image / 255
    image = np.expand_dims(image, axis=0)
    score = model.predict(image)
    return score*100
