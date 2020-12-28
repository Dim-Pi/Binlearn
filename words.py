from mysql.connector import connect
from sys import path
from library import convertep , convertpe , b_per
from atoken import DBInformation as DBI



sql = connect (
    user = DBI.usr(),
    password = DBI.pas(),
    database = DBI.dbn()
)



db = sql.cursor()
wdic = dict()


class word :


        
    def __init__ (self,en,fa,num,mode):
        self.mode = mode
        self.en = en
        self.fa = fa
        self.num = num
        

    def edit (self , newfa):
        try :
            self.fa = convertep (newfa)

            eeee = ''
            for q in self.fa.split(','):
                eeee += "%s," %q.strip()
            self.fa = eeee [:-1]

            db.execute ('update words set fa="%s" ,mode="True" where num=%i' %(convertpe(newfa),self.num))
            sql.commit()
            return True
        except :
            return False
    
    def add_fa (self ,newfa):
        try:
            
            self.fa = self.fa + ',' + convertep(newfa)

            eeee = ''
            for q in self.fa.split(','):
                eeee += ',%s' %q.strip()
            self.fa = eeee [:-1]

            db.execute ('update words set fa="%s" ,mode="True" where num=%i' %(convertpe(self.fa),self.num))
            sql.commit()
            self.fa = convertep (self.fa)
            return True
        except :
            return False



        
    def save (self):

        self.mode = 'True'
        db.execute ('update words set  mode="True"  where num=%i' %(self.num))
        sql.commit()


    

    
    def words():

        db.execute('select num ,en ,fa ,mode from words')


        for q in db.fetchall():
            wdic [q[0]] = word(q[1],convertep(q[2]),q[0],q[3])

        return wdic




    def unum (self):

        dd = self.num // 5 
        if dd == 0:
            return 5
        else:
            return dd








    def words_fa (q):



        if q == None :
            return None

        db.execute ('select num from words where fa="%s"'%convertpe(q)) 
        
        try :
            al = db.fetchall () [0]
        except Exception as e:
            return None
            

        return wdic[al[0]]
    






def lwords ():

    return wdic

















def mianword(word):
    
    db.execute('select en ,mode ,num from words where fa="%s"' %word )
    data = db.fetchall() [0]
    wordinfo = {'num':data[2],'mode':data[1],'en':data[0]}
    return  wordinfo












def words():

    db.execute('select num ,en ,fa ,mode from words')


    for q in db.fetchall():
        wdic [q[0]] = word(q[1],convertep(q[2]),q[0],q[3])

    return wdic









def find_num (fa):

    if type(fa) == list :
        ofa = ','.join(fa)
    else:
        ofa = fa


    uuuu = 1
    while uuuu == 1:
        try:

            db.execute('select num from words where fa="%s"' %ofa)
            rrrr = db.fetchall () [0]
            uuuu = 0
            return rrrr 
        except Exception as e:

            return None














def get_data () :

    from mysql.connector import connect
    from re import findall as find
    from bs4 import BeautifulSoup as bs
    from requests import get 
    from time import sleep

    urls = [ "https://lang.b-amooz.com/en/vocabulary/subcategories/643/lesson-1",
             "https://lang.b-amooz.com/en/vocabulary/subcategories/1690/lesson-2"
            ]


    bd = lambda x : True if find ('\d+',x) != [] and len (find ('\d+',x) ) == 1 and find ('\d+',x) [0] == str(x) else False

    num = 0

    for url in urls :
    #page = webdriver.Chrome()

        page = get(url)

        #sleep (3)

        qq = page.text

        z = bs(qq,'html.parser')

        x = z.findAll ('li')

        r = []

        b = 0

        for q in x :

            ok = find(r'\w+\s{0,1}\w*',q.text)
            if  len(ok) != 0 and bd (ok[0]):
                r.append(ok)

        yo = r[3:]


        y = []



        for s0 in yo :
            if b < 6 or not( s0[0] in ['1','2','3','4','5'] ) :
                po = ""
                for j in s0 :
                    if b_per (j) :
                        po += ' %s ' % j.strip()
                y.append (( s0[1].strip() , convertpe (po.strip())  ))

            b += 1


        
        sql = connect (
            user = DBI.usr(),
            password = DBI.pas(),
            database = DBI.dbn()
        )
        

        mydb = sql.cursor()

        

        for en , fa in y :

            num += 1


            mydb.execute ('INSERT INTO words (en  ,fa ,num ,mode) VALUES  ("%s"  ,"%s" ,%i ,"False") '  % (en  ,fa ,num))

            sql.commit()


            








words()












