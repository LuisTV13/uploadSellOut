from typing import NewType
import pandas as pd
import json
# from cred import getCred
# from sqlcon import execute_Sellout_dataframe,execute_Stock_dataframe

# # corporativo  = 'BDF'
# myHostname,myDatabase,myUsername,myPassword  =getCred(corporativo)




# dataframe1 = execute_Stock_dataframe(myHostname,myDatabase,myUsername,myPassword )

def generateJson(dataframe):
    
    #Declaramos el json
    info={}
    info['objects'] =[]
    #==============#
    df= dataframe
    #Colocar las columnas de la VIEW
    CANAL = df["canal"]
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
        AÑO.append(int(año))
    for mes in MONTH:
            MES.append(int(mes))   
    for unid in UNIDADES:
        UNID.append(str(unid))
    for soles in SOLES:
        SOLESS.append(str(soles))
    
   
   
    
    format_json={
        "canal" : CANAL,
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

def generateJsonStock(dataframe):
    
    #Declaramos el json
    info={}
    info['objects'] =[]
    #==============#
    df= dataframe
    #Colocar las columnas de la VIEW
    CANAL = df["CANAL"]
    YEAR = df["YEAR"]
    MONTH =df["MONTH"]
    CODPRODBDF = df["CODIGO_PRODUCTO_BDF"]
    NART= df["NART"]
    UNIDADES = df["STOCK_UNIDADES"]
    SOLES = df["STOCK_VALORIZADO"]
    AÑO =[]
    MES =[]
    UNID =[]
    SOLESS =[]
    for año in YEAR:
        AÑO.append(int(año))
    for mes in MONTH:
            MES.append(int(mes))   
    for unid in UNIDADES:
        UNID.append(str(unid))
    for soles in SOLES:
        SOLESS.append(str(soles))
    
   
   
    
    format_json={
        "canal" : CANAL,
        "codigo_producto_bdf": CODPRODBDF,
        "nart": NART,
        "year": AÑO,
        "month": MES,
        "stock_unidades": UNID,
        "stock_valorizado": SOLESS,
        
    }
    dataframe = pd.DataFrame(data=format_json)
    create_json = dataframe.to_json(orient='records')
    x = json.loads(create_json)
    for y in x :
        info['objects'].append(y)
    #Crear el json
    with open('output/variableStock.json','w') as outfile:
        json.dump(info,outfile)
   



# generateJsonStock(dataframe1)
    

    

    
    

