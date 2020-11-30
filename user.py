from sys import path
from list import list_get as glist
from mysql.connector import connect
from words import words_fa


sql = connect (
    user = 'pyprog',
    password = 'itpas',
    host = 'localhost',
    database = 'bot'

)

db = sql.cursor()




class user :

    

    def __init__ (self,id):

        db.execute('SELECT id ,name ,mode ,ready ,fmode ,fmode2 ,fmode3 ,mode2 ,word1,word2,word3,word4,word5 FROM user where id="%s"'%id)
        ius = db.fetchall() [0]

        self.id = id
        self.name = glist(ius ,1 ,'')
        self.mode = glist(ius ,2 ,'name')
        self.ready = glist(ius ,3 ,'False')
        self.fmode = glist(ius ,4 ,None)
        self.fmode2 = glist(ius ,5 ,None)
        self.fmode3 = glist(ius ,6 ,None)
        self.mode2 = glist(ius ,7 ,None)
        self.word1 = words_fa(glist(ius ,8 ,None))
        self.word2 = words_fa(glist(ius ,9 ,None))
        self.word3 = words_fa(glist(ius ,10 ,None))
        self.word4 = words_fa(glist(ius ,11 ,None))
        self.word5 = words_fa(glist(ius ,12 ,None))
        self.modeed = ''

    

    def users() :
        users1 = {}

        db.execute("SELECT * FROM user")
        alluser = db.fetchall()

        for q in alluser :
            users1[q[0]] = {'name' : q[1] , 'mode' : q[2]}
            
        
        return users1 
    
    def add_user (id ,name) :

        
        db.execute ('INSERT INTO user (id  ,name ,mode) VALUES  ("%s"  ,"%s" ,"%s") '  % (id ,name,'name'))
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

    

    def words (self):

        w1 = self.word1
        w2 = self.word2
        w3 = self.word3
        w4 = self.word4
        w5 = self.word5

        return [w1,w2,w3,w4,w5]



    def editmode (self):

        

        if self.modeed == '0':
            return self.word1
        elif self.modeed == '1':
            return self.word2
        elif self.modeed == '2':
            return self.word3
        elif self.modeed == '3':
            return self.word4
        elif self.modeed == '4':
            return self.word5
        
    



    def smodeed (self ,modeed):
        self.modeed = modeed




    def comeat (self , dic):

        for q in dic :
            if 'name' in dic:
                self.name = dic ['name']
            if 'ready' in dic:
                self.ready = dic ['ready']
            if 'mode' in dic:
                self.mode = dic ['mode']
            if 'fmode' in dic:
                self.fmode = dic ['fmode']
            if 'fmode2' in dic:
                self.fmode2 = dic ['fmode2']
            if 'fmode3' in dic:
                self.fmode3 = dic ['fmode3']
            if 'word1' in dic:
                self.word1 = dic ['word1']
            if 'word2' in dic:
                self.word2 = dic ['word2']
            if 'word3' in dic:
                self.word3 = dic ['word3']
            if 'word4' in dic:
                self.word4 = dic ['word4']
            if 'word5' in dic:
                self.word5 = dic ['word5']
 

        setor = 'update user set '
        
        for q in dic :
            setor +=  '%s="%s" , ' %(q,dic[q])
        
        setor = setor [ : len (setor) - 2]

        setor += ' where id="%s"'%self.id

        db.execute(setor)
        sql.commit()



    

    def chek_complet (self):

        db.execute('select word1,word2,word3,word4,word5 ,modint from user where id="%s"'%self.id )
        bar = db.fetchall() [0]
        if bar[0]=='True' and bar[1]=='True' and bar[2]=='True' :
            if bar[3]=='True' and bar[4]=='True':
                db.execute('update user set tday="True" , modint=%i where id="%s"'%(bar[5]+1,self.id))



    def get_words (self):

        sql = connect (
            user = 'pyprog',
            password = 'itpas',
            database = 'bot'
        )

        db = sql.cursor()
        db.execute('select tday from user where id="%s"' %self.id)
        m = db.fetchall() [0] [0]

        if m == 'True' :
            return True 
        elif m == 'False':
            db.execute('select word1 ,word2 ,word3 ,word4 ,word5 from user where id="%s"' %self.id)
            return db.fetchall()
        elif m == 'False2':
            db.execute('select word1 ,word2 ,word3 ,word4 ,word5 ,word6 ,word7 ,word8 ,word9 ,word10 from user where id="%s"' %self.id)
            return db.fetchall()




    



o = 1









