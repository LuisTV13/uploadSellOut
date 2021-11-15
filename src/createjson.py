from typing import NewType
import pandas as pd
import json
# from cred import getCred
# from sqlcon import execute_Sellout_dataframe

# corporativo  = 'BDF'
# myHostname,myDatabase,myUsername,myPassword  =getCred(corporativo)




#dataframe1 = execute_Sellout_dataframe(myHostname,myDatabase,myUsername,myPassword )

def generateJson(dataframe):
    
    #Declaramos el json
    info={}
    info['objects'] =[]
    #==============#
    df= dataframe
    #Colocar las columnas de la VIEW
    CODPRODBDF = df["codigo_producto_bdf"]
    NART= df["nart"]
    YEAR = df["year"]
    MONTH =df["month"]
    UNIDADES = df["unidades"]
    SOLES = df["soles"]
    AÑO =[]
    MES =[]
    UNID =[]
    SOLESS =[]
    for año in YEAR:
        AÑO.append(str(año))
    for mes in MONTH:
            MES.append(str(mes))   
    for unid in UNIDADES:
        UNID.append(str(unid))
    for soles in SOLES:
        SOLESS.append(str(soles))
    
   
   
    
    format_json={
        "codigo_producto_bdf": CODPRODBDF,
        "nart": NART,
        "year": AÑO,
        "month": MES,
        "unidades": UNID,
        "soles": SOLESS,
        
    }
    dataframe = pd.DataFrame(data=format_json)
    create_json = dataframe.to_json(orient='records')
    x = json.loads(create_json)
    for y in x :
        info['objects'].append(y)
    #Crear el json
    with open('output/variables.json','w') as outfile:
        json.dump(info,outfile)
    
# generateJson(dataframe1)
    

    

    
    

