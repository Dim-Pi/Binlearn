

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

        db.execute("SELECT * FROM users")
        alluser = db.fetchall()

        for q in alluser :
            users1[q[0]] = {'name' : q[1]}
            
        
        return users1 
    
    def add_user (self ,name) :

        self.mode = 'name'
        db.execute ('INSERT INTO users (id  ,name) VALUES  ("%s"  ,"%s") '  % (self.id ,name))
        sql.commit()



    def smode (self,m):

        if m == 0:
            return self.mode
        else :
            self.mode = m 
    

    def set_name (self,name0):

        self.name = name0
        db.execute ('update users set name = "%s" where id = "%s" '  % (name0 ,self.id))
        sql.commit()
        

    

    
    



o = 1









