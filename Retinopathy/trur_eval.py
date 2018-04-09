import cv2
import numpy as np
import keras
import sys
from keras.models import load_model

model = load_model("DR_Two_Classes_recall_0.7759.h5")

image_path = sys.argv[1]
image = cv2.imread(image_path)
image = cv2.resize(image,(256,256))
image = image / 255
image = np.expand_dims(image, axis=0)
score = model.predict(image)
print(score)
