from owlready2 import *
#import traduccionTweets

onto = get_ontology("/Users/victorbotti/Desktop/owl/DAO.owl")
onto.load()

clases = onto.classes()
instanciasTotal = []
propiedadesTotal = []
for clase in clases:
    ins = clase.instances()

    for instancia in ins:
        if instancia not in instanciasTotal:
            instanciasTotal.append(instancia)
        prop = instancia.has_slang_term
        for propiedad in prop:
            if propiedad not in propiedadesTotal:
                propiedadesTotal.append(propiedad)

f = open("/Users/victorbotti/Desktop/owl/terminosDrogas.txt", "w")
for ins in instanciasTotal:
    f.write(str(ins).replace("DAO.", "") + "\n")
for term in propiedadesTotal:
    f.write(term + "\n")
f.close()








