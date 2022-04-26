# Importamos la libreria json
import json

# Creamos un diccionario vacio
data = {}

# Seteamos la clave o llave "clientes" y le asignamos una lista vacia
data["clientes"] = []
# print(data) # Imprimimos para ver como es la estructura del diccionario

# Vamos agregando mediante append
data['clientes'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clientes'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clientes'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

# Imprimo para ver en la consola como queda la estructura
print(data)

# Finalmente se abre un archivo y se vuelca en el mismo los datos del diccionario utilizando json.dump().
""" with open("primer_json.json", 'w') as file:
    json.dump(data, file, indent=1) # Serializa un objeto python como un objeto json. Se apoya en la funcion write() y soporta file como objeto. """

# La otra forma de realizarlo
""" file = open("primer_json.json", 'w')
json.dump(data, file, indent=1)
file.close() """


# La lectura de archivos JSON es similar al proceso de escritura. 
""" with open("primer_json.json") as file:

    leer_json = json.load(file)
    print(leer_json)
    for cliente in leer_json['clientes']:
        print('Nombre:', cliente['first_name'])
        print('Apellido:', cliente['last_name'])
        print('Edad:', cliente['age'])
        print('Cantidad:', cliente['amount'])
        print('--------') """


#### Noten que utilizamos las funciones dump() y load(), estas son para operar con archivos.

#### Tambien tenemos las funciones dumps() y loads(), fijense que son diferentes, estas ultimas terminan con "s".
# Datos a escribir
diccionario = { 
  "id": "04", 
  "nombre": "Julia", 
  "departmento": "HR",
}


# Serializamos un objeto de Python (diccionario) a JSON
# La serialización/deserialización de objetos es un mecanismo por el cual un objeto pasa de ser objeto a texto, 
# es transportado a cualquier destino y finalmente se vuelve a transformar a objeto
json_object = json.dumps(diccionario, indent = 4) 
print(json_object)
print(type(json_object)) # El modulo json de Python siempre produce objetos tipo string --> https://frankgalandev.com/diferencias-entre-json-dump-vs-json-dumps/


#### Veremos el archivo datos.json y el main.py

#### Veremos el metodo loads() en el archivo get.py


# Opciones de la librería JSON
""" datos_persona = {"nombre": "Daniel", "apellido": "Rodríguez", "edad": 45, "monto": 456.76}
# Codificacion (recordar que JSON utiliza ASCII de manera predefinida)
print(json.dumps(datos_persona))
print(json.dumps(datos_persona, ensure_ascii=False))
# Ordenacion
print(json.dumps(datos_persona, ensure_ascii=False, sort_keys=True)) """