from flask import request
from flask import Response
from flask import Flask, render_template
app = Flask(__name__)

app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lcd08knAAAAAAAq0NyWa-ELFbTCw1ndk7zxKR3u'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lcd08knAAAAACKXlpCoMNtHaLlpS8_Mtx47vWE-'
# метод для обработки запроса от пользователя
@app.route("/apinet",methods=['GET', 'POST'])
def apinet():
 neurodic = {}
 # проверяем, что в запросе json данные
 if request.mimetype == 'application/json':
  # получаем json данные
  data = request.get_json()
  # берем содержимое по ключу, где хранится файл
  # закодированный строкой base64
  # декодируем строку в массив байт, используя кодировку utf-8
  # первые 128 байт ascii и utf-8 совпадают, потому можно
  filebytes = data['imagebin'].encode('utf-8')
  # декодируем массив байт base64 в исходный файл изображение
  cfile = base64.b64decode(filebytes)
  # чтобы считать изображение как файл из памяти, используем BytesIO
  img = Image.open(BytesIO(cfile))
  decode = neuronet.getresult([img])
  neurodic = {}
  for elem in decode:
   neurodic[elem[0][1]] = str(elem[0][2])
   print(elem)
 # пример сохранения переданного файла
 # handle = open('./static/f.png','wb')
 # handle.write(cfile)
 # handle.close()
 # преобразуем словарь в json-строку
 ret = json.dumps(neurodic)
 # готовим ответ пользователю
 resp = Response(response=ret,
 status=200,
 mimetype="application/json")
 # возвращаем ответ
 return resp

from google.colab import drive
drive.mount('/mntDrive')
import sys
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

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





