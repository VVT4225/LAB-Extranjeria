from extranjeria import *

if __name__ == "__main__":
    datos = lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    #print(datos)
    num_nac = numero_nacionalidades_distintas(datos)
    #print(num_nac)
    grupo_nacionalidades = set()
    grupo_nacionalidades.add("BULGARIA")
    donde_extranjeros = secciones_distritos_con_extranjeros_nacionalidades(datos,grupo_nacionalidades)
    print(donde_extranjeros)
