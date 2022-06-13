from mysql import  connector


config= {
    'user': 'root',
    'password': 'Admin2021',
    'host':'localhost',
    'database': 'recetas_bd',
    
       
}


def  create_connection():
    
    conn= None
    try:
         conn= connector.connect(**config)
     
    except connector.Error as err:
            print(f"error  at create_connection function: {err.msg}")
    return conn 