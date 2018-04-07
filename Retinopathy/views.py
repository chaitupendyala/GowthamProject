from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from . import models
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
        u = models.Eye_Images(image = request.FILES['image'])
        u.save()
        return HttpResponse("The Value is "+evaluate(u.id))
    else:
        return redirect("/check")

def evaluate(id_of_object):
    image_path = str(models.Eye_Images.get(id = id_of_object).path)
    image = cv2.imread(image_path)
    #image = cv2.resize(image,(256,256))
    image = image / 255
    image = np.expand_dims(image, axis=0)
    score = model.predict(image)
    return score*100
