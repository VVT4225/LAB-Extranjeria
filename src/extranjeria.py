import csv
from collections import namedtuple

RegistroExtranjeria = namedtuple('RegistroExtranjeria', 'distrito,seccion,barrio,pais,hombres,mujeres')

def lee_datos_extranjeria(ruta_fichero):
    res = []
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for i in lector:
            res.append(RegistroExtranjeria(i[0],i[1],i[2],i[3],int(i[4]),int(i[5])))
    return res

def numero_nacionalidades_distintas(datos):
    res = set()
    for i in datos:
        if i.pais not in res:
            res.add(i.pais)
    return len(res)

def secciones_distritos_con_extranjeros_nacionalidades(datos,paises):
    tupladistrito = namedtuple("tupladistrito","distrito,seccion")
    res = []
    for i in datos:
        if i.pais in paises:
            res.append(tupladistrito(i.distrito, i.seccion))
    return sorted(res)