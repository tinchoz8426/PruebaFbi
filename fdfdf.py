def funcion_prueba():
    
    class Persona():
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
        
        def get_datos(self):
            return f"Soy {self.nombre} y tengo {self.edad}"

    return Persona()


funcion_prueba().edad = 4
