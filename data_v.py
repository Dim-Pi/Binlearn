from sys import path 
from mysql.connector import connect 
from time import sleep , localtime
from list import list_get as lget
from core import send_message as osend
from atoken import DBInformation as DBI







sql = connect (
    user = DBI.usr(),
    password = DBI.pas(),
    database = DBI.dbn()
)


db = sql.cursor()

inl = []

def gen ():
    while True :
        sleep (3)
        yield  list(localtime() ) [3]


def read_to_send (id):

    db.execute ('select modint from user where id="%s"' %id)
    num = db.fetchall() [0] [0]
    
    tdata = []
    
    

    db.execute ('select * from words where num=%i' %q)
    tdata.append (db.fetchall() [0])

    slist = list()
    for q in tdata :
        slist.append ([q[0],q[1]])


    return slist



for now in gen():
    
    db.execute ('select * from user')

    mdata = db.fetchall()

    

    for data in mdata:

        if data [9] == 'False'  :
            inl = ['6','7','8','9','10']
        else:
            inl = ['1','2','3','4','5']

        ooo = 0
        id = data [0]
        if str(data [len(data)-1]) == '5.2'   :

            smsg = 'اینم از پنج تای امروزت'
            ooo = read_to_send(id)
        
        elif (now == 5 and lget (data ,3,'') == 'True' ) :

            smsg = 'سلام چطوری ؟ اینم از پنج تای امروزت'
            ooo = read_to_send(id)

        if ooo != 0 :

            
            for rrr  in range(0,5) :
                
                q = ooo[rrr]
                
                smsg += '\n%i_%s' %(rrr + 1 , q[0])
                
                l = inl[rrr-1]


                
                
                
                db.execute('update user set word%s="%s" , tday="False"  where   id="%s"' %(l,q[1],id) )
                sql.commit()
            
            osend ({'type':'TEXT','body':smsg,'to':id})

            db.execute('update  user set flo="1.1"  where id="%s"' %id )
            sql.commit()







