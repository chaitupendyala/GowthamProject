from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Eye_Images
import cv2
import numpy as np
import keras
from keras.models import load_model

model = load_model("/home/chaitanya/Desktop/DDR/DR_Two_Classes_recall_0.7759.h5")

def enter_image(request):
    return render(request,"Retinopathy/main.html",{})

@csrf_exempt
def store_image(request):
    if request.method == "POST":
        u = Eye_Images(image = request.FILES['image'])
        u.save()
        return_val = evaluate(u.id)
        print str(return_val[0]+" "+return_val[1])
        return HttpResponse("<h1>Class 1 resemblence is :"+str(return_val[0])+"<br/>"+"Class 2 resemblence is :"+str(return_val[1]))
    else:
        return redirect("/check")

def evaluate(id_of_object):
    image_path = str(Eye_Images.objects.get(id = id_of_object).image.path)
    print image_path
    image = cv2.imread(image_path)
    if image is not None:
        print "hello"
        image = cv2.resize(image,(256,256))
        image = image / 255
        image = np.expand_dims(image, axis=0)
        score = model.predict(image)
        return score*100
    else:
        return [0.0,0.0]
