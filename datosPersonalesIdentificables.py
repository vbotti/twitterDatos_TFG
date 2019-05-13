import re


def datos(tweetList):
    for tweet in tweetList:
        text = tweet[1]

        email = re.search(r'[\w\.-]+@[\w\.-]+', text)

        tweet_no_users = re.sub(r'\w*@\w*', '', text)
        tweet_no_hashtags = re.sub(r'#\w*', '', tweet_no_users)
        text = re.sub(r'https?:\/\/.*\/\w*', '', tweet_no_hashtags)

        telefono = re.search(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
                             ,
                             text)  # 7 o 10 digitos (sirve para cuentas bancarias, ttajetas de credito, dni y numeros de telefono)
        telefonoEsp = re.search(r'[697]\d{1,2}.\d{2,3}.\d{2,3}.\d{0,2}', text)  # 9 digitos (telefono españa)

        dni = re.search(r'[0-9]{8,8}[A-Za-z]', text)  # 8 digitos + letra al final

        fecha1 = re.search(r'(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[0-2])\1\d{4}$', text)  # dd-mm-aaaa
        fecha2 = re.search(r'(?:0?[1-9]|1[0-2])([\-/.])(3[01]|[12][0-9]|0?[1-9])\1\d{4}$', text)  # mm-dd-aaaa
        fecha3 = re.search(r'\d{4}([\-/.])(0?[1-9]|1[0-2])\1(3[01]|[12][0-9]|0?[1-9])$', text)  # aaaa-mm-dd

        codpostal = re.search(r'(?:0[1-9]|[1-4]\d|5[0-2])\d{3}', text)  # codigo postal desde el 01000 al 52999 (España)
        if str(email) != "None" or str(telefonoEsp) != "None" or str(telefono) != "None" or str(dni) != "None" \
                or str(fecha1) != "None" or str(fecha2) != "None" or str(fecha3) != "None" or str(codpostal) != "None":

            tweet[2][5] = 1 #Vector de etiquetas de 7

    return tweetList



#print(datos([[917564856647274496, '@CarmenV86637217 pepe@gmail Es superbonito tu gatito bafkertomizado....', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]))
