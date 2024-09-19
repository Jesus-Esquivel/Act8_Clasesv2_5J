print("Clases v2 Esquivel Adrian")
# Zona de clase
class Datos:
    # el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso   
    def mi_lista(self):
        canciones=["La patrulla","HOLLYWOOD","Por Las Noches"]
        print(canciones)
        for music in canciones:
            print(music) 
# Zona de Tuplas
    def music(self):
        misc=["Puño de tierra", "La patrulla", "HOLLYWOOD"]
        print(misc)
        for x in misc:
            print(x)
# Zona de Dictionaries
    def my_musica(self):
        mucs={
            "Nombre": "La patrulla",
            "genero": "corrido",
            "año": 2024}
        print(mucs)
        for x, y in mucs.items():
            print(x, y) 
# Zona de  Sets
    def musc(self):
        cancion={"Luna", "No se va","Tarde"}
        print(cancion)
        for x in cancion:
            print(x)
# Creaccion de objeto
info=Datos(1.90,60)
# Utilizando el obj.
print("Estatura: ",info.estatura)
print("Peso: ",info.peso)
print("Lista de Canciones de Esquivel Adrian")
info.mi_lista()
print("Tuplas de Canciones de Esquivel Adrian")
info.music()
print("Diccionarios de Canciones de Esquivel Adrian")
info.my_musica()
print("Set de Canciones de Esquivel Adrian")
info.musc()
