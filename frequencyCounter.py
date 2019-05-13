from collections import Counter
import utils

with open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria6.json", 'r') as fichero:
    cont = fichero.read()
    arr = eval(cont)
    lista = arr
l=[]
for texto in lista:
    l.append(texto[1])
print(lista)
x = utils.clean_data_from_list(l)
palabras = []
for tweet in x:
    for palabra in tweet:
        palabras.append(palabra)

counts = Counter(palabras).most_common(20)
print("-------------------------")
print("-------------------------")
print(counts)
