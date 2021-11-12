import pyodbc 
import pandas as pd
import sys
#from cred import getCred

#corporativo  = 'BDF'
# myHostname,myDatabase,myUsername,myPassword  =getCred(corporativo)

# print(myHostname,myDatabase,myUsername,myPassword)
def execute_Sellout_dataframe(myHostname,myDatabase,myUsername,myPassword):
     try:
          
          conn_string = 'DRIVER={SQL Server};SERVER='+myHostname+';DATABASE='+myDatabase+';UID='+myUsername+';PWD='+ myPassword
          conn = pyodbc.connect(conn_string)

          with conn:
                cursor = conn.cursor()
                query = "SELECT TOP 10 * FROM Clientes"
                cursor.execute(query)
                conn.commit()
                #print("Ejecutando query")
                table_frame = pd.read_sql_query(query, conn)
                #print("Query ejecutada : "+query)
                return table_frame
     except:
        print("Unexpected error en func 'exec_query': ", sys.exc_info())
        return 'Error en exec_query'
   
#print(execute_Sellout('BDF'))