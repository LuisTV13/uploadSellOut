def read_Cred():
    objeto = {
        "BDF" : {
        "myHostname" : "51.222.82.148",
        "myDatabase": "STRATEGIO_BRUTO_BDF",
        "myUsername": "sa",
        "myPassword": "9aj8d2.1ej92-huF!HFDH-8hy91e2",
      }
    }
    return objeto


def getCred(BD):
    objeto  = read_Cred()
    myHostname  = objeto[BD]["myHostname"]
    myDatabase  = objeto[BD]["myDatabase"]
    myUsername  = objeto[BD]["myUsername"]
    myPassword  = objeto[BD]["myPassword"]

    return myHostname,myDatabase,myUsername,myPassword
