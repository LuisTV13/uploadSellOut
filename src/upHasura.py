import requests
import json
#Creds HASURA
UrlRest ="https://graph.sop.strategio.cloud/v1beta1/relay"
headers ={"x-hasura-admin-secret"  : "x5cHTWnDb7N2vh3eJZYzamgsUXBVkw",
           "content-type":"application/json"}



#Funcion
def insert_sellIn(query,variables):
    request = requests.post(UrlRest, json={'query': query ,"variables":variables}, headers=headers,)
    if request.status_code == 200:
        print("Ingresado Correctamente")
        return request.json()
        
    else :
        raise print(Exception('Error Mutacion'))


#insert_sellIn(query,variables)

