# todo: Задан словарь, его значения необходимо внести по соответствущим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body download="alert(?)">

  <p>?</p>

 </body>
</html>
"""

template = template.split('\n')

for i in range(len(template)):
    for j_key in page.keys():
        if '?' in template[i] and j_key in template[i]:
            template[i] = template[i].replace('?', page[j_key])

template = '\n'.join(template)
print(template)
fd = open('index.html', mode='wt', encoding='UTF-8')
fd.writelines(template)
fd.close()