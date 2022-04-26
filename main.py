import json

file = open("datos.json", "r")
content = file.read()

js = json.loads(content)
# Imprimimos lo que obtenemos de "nombre" del contenido de datos.json
print(js["nombre"])
# Imprimimos todo lo que obtenemos del contenido de datos.json
print(content) # OJO, que este content no esta transformado todavia a objeto de python, el que esta transformado es js, vamos a imprimirlo aca abajo, y tambien el type para
# que vean que ya lo transformo a objeto de Python (o sea, tipo diccionario):
print(type(content))
print(js)
print(type(js))

file.close()