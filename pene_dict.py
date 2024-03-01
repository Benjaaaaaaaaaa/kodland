pene_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "xd": "Risa",
            "melo": "genial, bueno",
            "parcero": "amigo o conocido"
            }
           
palabra= input("Que palabra no entiendes?")

if palabra in pene_dict:
    print(palabra+ "=", pene_dict[palabra])
else:
    print("no tengo la definicion de esa palabra")
    clave = random.choice(pene_dict.key() )
    print(clave+ ":", pene_dict[clave])
