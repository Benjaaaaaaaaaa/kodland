import random
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "xd": "Risa",
            "melo": "genial, bueno",
            "parcero": "amigo o conocido"
            }
           
palabra= input("Que palabra no entiendes?")

if palabra in pene_dict:
    print(palabra+ "=", meme_dict[palabra])
else:
    print("no tengo la definicion de esa palabra")
    clave = random.choice(pene_dict.key() )
    print(clave+ ":", meme_dict[clave])
