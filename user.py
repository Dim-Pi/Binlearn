from sys import path
from list import list_get as glist
from mysql.connector import connect

sql = connect (
    user = 'root',
    password = '41148',
    host = 'localhost',
    database = 'bot'

)

db = sql.cursor()




class user :

    

    def __init__ (self,id,name):
        self.id = id
        self.name = name
        self.mode = '0'

    

    def users() :
        users1 = {}

        db.execute("SELECT * FROM user")
        alluser = db.fetchall()

        for q in alluser :
            users1[q[0]] = {'name' : q[1] , 'mode' : q[2]}
            
        
        return users1 
    
    def add_user (self ,name) :

        self.mode = 'name'
        db.execute ('INSERT INTO user (id  ,name ,mode) VALUES  ("%s"  ,"%s" ,"%s") '  % (self.id ,name,self.mode))
        sql.commit()



    def smode (self,m):

        if m == 0:
            return self.mode
        else :
            
            self.mode = m 
            db.execute ('update user set mode = "%s" where id = "%s" '  % (self.mode ,self.id))
            sql.commit()

    def set_name (self,name0):

        self.name = name0
        db.execute ('update user set name = "%s" where id = "%s" '  % (name0 ,self.id))
        sql.commit()


    def get_id (id):

        db.execute('SELECT * FROM user where id="%s"' %id)
        iuser = db.fetchall()

        return glist(glist(iuser,0,''),1,'')

        

    

    
    



o = 1









