{% extends "bootstrap/base.html" %} 
{% import "bootstrap/wtf.html" as wtf %}
<!-- задаем заголовок страницы --> 
{% block title %}This is an page{% endblock %}
<!-- блок body --> 
{% block content %} 
{{ wtf.quick_form(form, method='post',enctype="multipart/form-data", action="net") }}
<!-- один из стандартных тегов html – заголовок второго уровня --> 
<h2>Classes: </h2> 
<!—проверяем, есть ли данные классификации --> 
{% if neurodic %}
 <!-- запускаем цикл прохода по словарю и отображаем ключ-значение -->
 <!-- классифицированных файлов -->
 {% for key, value in neurodic.items() %}
 <h3>{{key}}: {{value}}</h3> 
 {% endfor %}
{% else %}
 <h3> There is no classes </h3> 
{% endif %}
<h2>Image is here: </h2> 
<!-- отображаем загруженное изображение с закругленными углами --> 
<!-- если оно есть (после submit) --> 
{% if image_name %}
 <p>{{image_name}}
 <p><img src={{image_name}} class="img-rounded" alt="My Image" width = 224 height=224 />
{% else %}
 <p> There is no image yet </p> 
{% endif %}
{% endblock %} 
