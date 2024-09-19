print("Clases v2 Esquivel Adrian")
# Zona de clase
class Datos:
    # el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso   
    def mi_lista(self):
        canciones=["La patrulla","HOLLLYWOOD","Por Las Noches"]
        print(canciones)
        for music in canciones:
            print(music) 
# Zona de Dictionaries
my_musica =	{
    "Nombre": "La patrulla",
    "año": "2024",
    "genero": "corrido" 
}
# Zona de Tuplas
music = ("Luna", "La patrulla", "HOLLYWOOD")
# Zona de  Sets
mus = {"Luna", "No se va","Tarde"}
# Creaccion de objeto
info=Datos(1.90,60)
# Utilizando el obj.
print("Estatura: ",info.estatura)
print("Peso: ",info.peso)
print("Lista de Canciones de Esquivel Adrian")
info.mi_lista()
print("")
for x in my_musica.values():
    print(x)
print("")    
for x in music:
    print(x)
print("")
for x in mus:
    print(x)