from src.cred import getCred
from src.sqlcon import execute_Sellout_dataframe
from src.createjson  import generateJson
from src.upHasura import insert_sellIn
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
mutation prueba($objects: [prueba1_insert_input!]!) {
  insert_prueba1(objects: $objects, on_conflict: {constraint:prueba1_pkey}) {
    returning {
      cogiCli
    }
  }
}


"""
#JSON
archivo = open('output/variables.json')
variables = json.load(archivo)
#===========================================#
insert_sellIn(query,variables)


