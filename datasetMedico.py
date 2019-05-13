f = open("/Users/victorbotti/Desktop/DatasetMedico/fd-export.csv")
fich = f.read()
f.close()

fich = fich.split("\n")
fich.pop(0)
sintomas = []
f = open("/Users/victorbotti/Desktop/DatasetMedico/enfermedadesCondition.txt", "w")
cont = 0
for paciente in fich:
    paciente = paciente.split(",")
    try:
        if paciente[6] == "Condition":
            cont = cont + 1
            sintomas.append(paciente[7].lower())
    except: print(paciente)
noRep = sorted(set(sintomas))
f.write(str(noRep))
print(cont)
f.close()

