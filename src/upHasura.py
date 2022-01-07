import requests
import json
#Creds HASURA
UrlRest ="https://graph.sop.strategio.cloud/v1beta1/relay"
headers ={"x-hasura-admin-secret"  : "x5cHTWnDb7N2vh3eJZYzamgsUXBVkw",
           "content-type":"application/json"}

#Funcion
def insert_sellOut(query,variables):
    request = requests.post(UrlRest, json={'query': query ,"variables":variables}, headers=headers,)
    if request.status_code == 200:
        print(request.json())
        return request.json()
        
    else :
        raise print(Exception('Error Mutacion'))

def insert_Stock(query,variables):
    request = requests.post(UrlRest, json={'query': query ,"variables":variables}, headers=headers,)
    if request.status_code == 200:
        print(request.json())
        return request.json()
        
    else :
        raise print(Exception('Error Mutacion'))


def deleteTable(query):
    request = requests.post(UrlRest, json={'query': query}, headers=headers,)
    if request.status_code == 200:
        print(request.json())
        return request.json()
        
    else :
        raise print(Exception('Error Mutacion'))


# archivo = open('output/variables.json')
# variables = json.load(archivo)

# insert_sellOut(query,variables)

