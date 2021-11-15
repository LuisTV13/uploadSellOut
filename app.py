from src.cred import getCred
from src.sqlcon import execute_Sellout_dataframe
from src.createjson  import generateJson
from src.upHasura import insert_sellOut
import json 

corporativo ='BDF'
#ObteniendoCredenciales
myHostname,myDatabase,myUsername,myPassword  =getCred(corporativo)
#Dataframe de la View
dataframe = execute_Sellout_dataframe(myHostname,myDatabase,myUsername,myPassword)
#GenerarJSON
generateJson(dataframe)
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
#JSON
archivo = open('output/variables.json')
variables = json.load(archivo)
#===========================================#
insert_sellOut(query,variables)


