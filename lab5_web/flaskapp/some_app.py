from flask import request
from flask import Response
from flask import render_template 
#app = Flask(__name__)

import sys
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#наша новая функция сайта
@app.route("/data_to") 
def data_to():
 #создаем переменные с данными для передачи в шаблон
 some_pars = {'user':'Ivan','color':'red'} 
some_str = 'Hello my dear friends!'
 some_value = 10
 #передаем данные в шаблон и вызываем его
 return render_template('simple.html',some_str = some_str,
 some_value = some_value,some_pars=some_pars) 

from google.colab import drive
drive.mount('/mntDrive')

s = input("Введите название картинки 'jpg'")
image_box=Image.open('/mntDrive/My Drive/python/dataf/'+s+'.jpg')

x = np.asarray(image_box)
y = np.asarray(image_box)
#x =x[:,:150,0:3] -изменяем размер
s = input("Введите яркость 'до 200' ")
s=int(s)
x =x/(200-s)  # деление на число задаёт яркость чем меньше тем ярче

fig = plt.figure(figsize=(5,5))
viewer1 = fig.add_subplot(1,2,1)
viewer1.imshow(y) # делаем график изображения
viewer2 = fig.add_subplot(1,2,2)
viewer2.imshow(x) # делаем график изображения
fig.show()



