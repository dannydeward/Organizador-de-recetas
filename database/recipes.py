from mysql import connector
from database.connection import create_connection



def  insert(data):
    conn = create_connection()
    sql= """INSERT INTO recetas (title, category, guide_url, budget, img_path,
                      ingredients, directions)
    
             
            VALUES(%s, %s, %s, %s, %s, %s, %s)"""
   
        
    try:
        cur=conn.cursor() 
        cur.execute(sql, data)      
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_recuoe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
    
def  select_all():
    conn = create_connection()
    sql= """ SELECT id,img_path, title, category FROM recetas"""
   
        
    try:
        cur=conn.cursor() 
        cur.execute(sql)      
        recipes= cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at selec_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
        

def select_by_id(_id):
    conn = create_connection()
    sql= f""" SELECT * FROM recetas WHERE id={_id}"""
   
        
    try:
        cur=conn.cursor() 
        cur.execute(sql)      
        recipe= cur.fetchone()
        return recipe
    except connector.Error as err:
        print(f"Error at selec_by_id function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def update(_id, data):
    conn=create_connection()    
    sql=f"""UPDATE recetas SET
                                title= %s,
                                category= %s,
                                guide_url= %s,
                                budget= %s,
                                img_path= %s,
                                ingredients= %s,
                                directions= %s
                                
    
             
          WHERE id = {_id}"""
   
        
    try:
        cur=conn.cursor() 
        cur.execute(sql, data)      
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at update recipe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


            
def select_by_parameter(param):
    conn = create_connection()
    param=f"%{param}%"
    sql= """ SELECT id,img_path,title,category FROM recetas WHERE  title LIKE %s OR category like %s"""
   
        
    try:
        cur=conn.cursor() 
        cur.execute(sql,(param,param))      
        recipes= cur.fetchall()
        return recipes
    except connector.Error as err:
        print(f"Error at selec_by_parasm function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
        
def delete(_id):
    conn=create_connection()    
    sql=f"""DELETE FROM  recetas                       
            WHERE id = {_id}"""
           
    try:
        cur=conn.cursor() 
        cur.execute(sql)      
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete recipe function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()