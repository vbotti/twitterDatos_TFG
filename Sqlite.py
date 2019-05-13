import sqlite3
def asignaCategorias(listaTags):
    x=''
    switcher = {
    0: '7',
    1: "Salud",
    2: "Drogas/Alcohol",
    3: "Emoción",
    4: "Ataques Personales",
    5: "Estereotipar",
    6: "Detalles de relación",
    7: "Detalles personales",
    8: "Datos personales identificables",
    9: "Neutral/objetiva",

    }
    for tag in listaTags:

        x += switcher[int(tag)] + ", "

    return x

def sqliteFuncion(consulta):
    x = []
    con_bd = sqlite3.connect('/Users/victorbotti/Desktop/BD_sqlite/db.sqlite3')
    cursor_agenda = con_bd.cursor()
    cursor_agenda.execute(consulta)
    for registro in cursor_agenda:
        x.append(str(registro)[1:-2])
    return x
    cursor_agenda.close()
    con_bd.close()

def sqliteFuncionListas(consulta):
    x = []
    con_bd = sqlite3.connect('/Users/victorbotti/Desktop/BD_sqlite/db.sqlite3')
    cursor_agenda = con_bd.cursor()
    cursor_agenda.execute(consulta)
    for registro in cursor_agenda:
        #x.append(str(registro)[1:-2])
        x.append(list(registro))
    return x
    cursor_agenda.close()
    con_bd.close()
def recuperarEtiquetas(id_str):
    lista = []
    lista2 = []
    con_bd = sqlite3.connect('/Users/victorbotti/Desktop/BD_sqlite/db.sqlite3')
    cursor_agenda = con_bd.cursor()
    cursor_agenda.execute("Select tags From tagger_tweettag WHERE tweet_id LIKE "+ id_str)
    for num in cursor_agenda:
        lista.append(num[0])
    return lista


