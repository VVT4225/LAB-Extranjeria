from extranjeria import *

if __name__ == "__main__":
    datos = lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    #print(datos)
    num_nac = numero_nacionalidades_distintas(datos)
    print(num_nac)
