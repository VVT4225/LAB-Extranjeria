from extranjeria import *

if __name__ == "__main__":
    datos = lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    #print(datos)
    num_nac = numero_nacionalidades_distintas(datos)
    #print(num_nac)
    grupo_nacionalidades = set()
    grupo_nacionalidades.add("BULGARIA")
    donde_extranjeros = secciones_distritos_con_extranjeros_nacionalidades(datos,grupo_nacionalidades)
    #print(donde_extranjeros)
    total_ext_pais = total_extranjeros_por_pais(datos)
    #print(total_ext_pais)
    ranking = top_n_extranjeria(datos, 3)
    print(ranking)
