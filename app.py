from src.cred import getCred
from src.sqlcon import execute_Sellout_dataframe, execute_Stock_dataframe
from src.createjson  import generateJson, generateJsonStock
from src.upHasura import deleteTable, insert_Stock, insert_sellOut
import json 

corporativo ='BDF'
#ObteniendoCredenciales
myHostname,myDatabase,myUsername,myPassword  =getCred(corporativo)
#Dataframe de la View



dataframe = execute_Sellout_dataframe(myHostname,myDatabase,myUsername,myPassword)
dataframeStock = execute_Stock_dataframe(myHostname,myDatabase,myUsername,myPassword)

#GenerarJSON
generateJson(dataframe)
generateJsonStock(dataframeStock)
#=================================================#
#SubirAlHASURA
    #QUERY
query = """
mutation sellout($objects: [Sell_out_insert_input!]!) {
  insert_Sell_out(objects: $objects, on_conflict: {constraint:Sell_out_pkey, update_columns:nart}) {
    returning {
      codigo_producto_bdf
    }
  }
}



"""
queryDeleteStock = """
mutation delete_all_stock_strategio {
delete_Stock_strategio (
where: {}
) {
affected_rows
}
}


"""

queryDeleteSellout = """
mutation delete_all_sellout {
delete_Sell_out (
where: {}
) {
affected_rows
}
}

"""



queryStock = """
mutation STOCK($objects: [Stock_strategio_insert_input!]!) {
  insert_Stock_strategio(objects: $objects, on_conflict: {constraint:Stock_strategio_pkey, update_columns:nart}) {
    returning {
      codigo_producto_bdf
    }
  }
}




"""
deleteTable(queryDeleteSellout)
deleteTable(queryDeleteStock)



#JSON
archivo = open('output/variables.json')
variables = json.load(archivo)
#===========================================#

#JSON
archivoStock = open('output/variableStock.json')
variablesStock = json.load(archivoStock)
#===========================================#




insert_sellOut(query,variables)

insert_Stock(queryStock,variablesStock)



