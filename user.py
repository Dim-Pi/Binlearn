from sys import path
from list import list_get as glist
from mysql.connector import connect
from words import word
from core2 import send_message as osend
from timerdef import timerdef
from atoken import DBInformation as DBI







words_fa = word.words_fa


sql = connect (
    user = DBI.usr(),
    password = DBI.pas(),
    database = DBI.dbn()
)


db = sql.cursor()




class user :

    udic = dict()

    def __init__ (self,id):

        db.execute('SELECT id ,name ,mode ,ready ,fmode ,fmode2 ,fmode3 ,mode2 ,word1,word2,word3,word4,word5 ,sendtime FROM user where id="%s"'%id)
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
        self.sendtime = int(ius [13])
        self.modeed = ''

    

    def users() :
        users1 = {}

        db.execute("SELECT * FROM user")
        alluser = db.fetchall()

        for q in alluser :
            users1[q[0]] = {'name' : q[1] , 'mode' : q[2]}
            
        
        return users1 
    

    def add_user (id ,name) :

        
        db.execute ('INSERT INTO user (id  ,name ,mode ,word6 ,word7 ,word8 ,word9 ,word10 ,sendtime) VALUES  ("%s"  ,"%s" ,"%s" ,"False" ,"False" ,"False" ,"False" ,"False" ,5) '  % (id ,name,'name'))
        sql.commit()



    def wsync (self):


        db.execute ('select word1 ,word2 ,word3 ,word4 ,word5 from user where id="%s"'   %self.id)
        w0rds = db.fetchall() [0]



        self.word1 = words_fa(glist(w0rds ,0 ,None))
        self.word2 = words_fa(glist(w0rds ,1 ,None))
        self.word3 = words_fa(glist(w0rds ,2 ,None))
        self.word4 = words_fa(glist(w0rds ,3 ,None))
        self.word5 = words_fa(glist(w0rds ,4 ,None))
        









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





    def send (self ,data):

        osend ({'to':self.id,'body':data.get('body',''),'type':'TEXT','keyboard':data.get('keyboard',[])})


    def word_save(self):

        self.modeed.save()



 
 
 
    def sync (self):



        db.execute ("select modint from user where id='%s' "  %  str(self.id))
        n = db.fetchall() [0] [0]

        tdata = []

        for q  in  range( n*5 +1 , ((n + 1)*5) +1 ):

            db.execute ('select fa from words where num=%i' %q)
            ert = db.fetchall() [0]
            tdata.append (ert [0])

        slist = []

        q = 0

        for qfa in tdata :

            q += 1

            db.execute('update user set word%i="%s" where id="%s" '
                    %(                      q  ,qfa          ,self.id         ) 
            )
            sql.commit()

            











    def okword (self ,num):

        db.execute ('update user set word%i="Completed!!"  where id="%s"'  %(int(num) + 5 ,self.id)  )
        sql.commit()











    def wait (self):

        self.smode ('wait')
        try :
            f = self.flo 
        except :
            f = 0
        if f != 1.1 :
            self.flo = 4.7
            db.execute ('update user set flo=4.7 where id="%s"'  %self.id)
            sql.commit()
            timerdef(imode=1)









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
            if 'sendtime' in dic:
                self.sendtime = dic ['sendtime']
            if 'flo' in dic:
                self.flo = dic ['flo']
            
 

        setor = 'update user set '
        
        for q in dic :
            if type(dic[q]) == str :
                setor +=  '%s="%s"   ,' %(q,dic[q])
            elif type(dic[q]) == int :
                setor +=  '%s=%i   ,' %(q,dic[q])
            elif type(dic[q]) == float :
                setor +=  '%s=%f   ,' %(q,dic[q])


        setor = setor [ : len (setor) - 2]

        setor += ' where id="%s"'%self.id

        db.execute(setor)
        sql.commit()
        dbsync()




    def next (self) :

        dbsync()

        db.execute("select modint from user where id='%s'" %self.id)
        bar = db.fetchall () [0] [0]
        
        
        db.execute("update user set tday='True' , modint=%i ,word6='%s' ,word7='%s' ,word8='%s' ,word9='%s' ,word10='%s' where id='%s'"  %(  int( bar )+1 ,'False' ,'False' ,'False' ,'False' ,'False' ,self.id)   )
        sql.commit()
        
        







    

    def chek_complet (self):

        db.execute('select word6,word7,word8,word9,word10 ,modint from user where id="%s"'%self.id )
        bar = db.fetchall() [0]
        if bar[1]=='Completed!!' and bar[2]=='Completed!!' and bar[3]=='Completed!!' :
        
            if bar[4]=='Completed!!' and bar[0]=='Completed!!':
                
                return True

        return False


    def get_words (self):

        sql = connect (
            user = DBI.usr(),
            password = DBI.pas(),
            database = DBI.dbn()
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






    def b_word (self ,word):

        unum = word.unum()
        dbsync()
        db.execute("select word%i from user where id='%s'"%(unum+5,self.id))
        try :
            v = db.fetchall() [0] [0]
            if v == "Completed!!" :
                return True
            else:
                return False
        except:
            pass


        

    def block (self) :

        if self.mode != 'block':
            self.bacmode = self.mode
            self.smode ('block')

        else :
            self.smode (self.bacmode)
            










    def dontwords(self):

        dbsync()
        alist = []
        list = self.words()
        for q in list :
            if not self.b_word(q):
                alist.append (q)
        
        return alist






    def __del__ (self) :
        dbsync ()
        db.execute("delete from user where id='%s'"%self.id)














o = 1
def dbsync():

    
    sql = connect (
        user = 'pyprog',
        password = 'itpas',
        host = 'localhost',
        database = 'bot'

 )

    db = sql.cursor()












