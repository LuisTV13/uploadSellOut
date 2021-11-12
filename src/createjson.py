from typing import NewType
import pandas as pd
import json


#dataframe1 = execute_Sellout_dataframe('BDF')

def generateJson(dataframe):
    
    #Declaramos el json
    info={}
    info['objects'] =[]
    #==============#
    df= dataframe
    #Colocar las columnas de la VIEW
    CODIGODT = df["CodigoDistribuidor"]
    CODCLI = df["CodigoCliente"]
    
    format_json={
        "codigoDtt": CODIGODT,
        "cogiCli": CODCLI
    }
    dataframe = pd.DataFrame(data=format_json)
    create_json = dataframe.to_json(orient='records')
    x = json.loads(create_json)
    for y in x :
        info['objects'].append(y)
    #Crear el json
    with open('output/variables.json','w') as outfile:
        json.dump(info,outfile)
    
#generateJson(dataframe1)
    

    

    
    

