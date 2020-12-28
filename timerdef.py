from sys import path 
from mysql.connector import connect 
from time import sleep
from list import list_get as lget
from core2 import send_message as osend
from library import cnow
from atoken import DBInformation as DBI









def sync ():

    try:    
        sql.disconnect()
    except:
        pass

    sql = connect (
    user = DBI.usr(),
    password = DBI.pas(),
    database = DBI.dbn()
    )

    db = sql.cursor()

    return sql , db 
  























print ('start')

sync ()

print ('connected')


inl = []








def read_to_send (id):

    sql , db = sync ()

    db.execute ('select modint from user where id="%s"' %id)
    num = db.fetchall() [0] [0]
    
    tdata = []
    
    for q in range( num*5 +1 , ((num + 1)*5) +1 ):

        db.execute ('select * from words where num=%i' %q)
        ert = db.fetchall() 
        tdata.append (ert [0])

    slist = list()
    for q in tdata :
        slist.append ([q[0],q[1]])


    return slist









def read_to_send2 (id):

    db.execute ('select word1 ,word2 ,word3 ,word4 ,word5 from user where id="%s"' %id)
    num = db.fetchall() [0] 
    


    return num











def timerdef (imode=0): 
    now = cnow()

    sql , db = sync()


    db.execute ('select flo , id , ready , mode ,word6 ,word7 ,word8 ,word9 ,word10 ,qmode ,sendtime ,tday ,modint from user')

    mdata = db.fetchall()

    

    for data in mdata:

        
    
        
        inl = ['1','2','3','4','5']


        ooo = 0
        id = data [1]

        if data[9]  == '<.>':
            if str(data [0]) == '5.2'   :

                smsg = 'اینم از پنج تای امروزت'
                ooo = read_to_send(id)
        
            elif (now == lget (data ,10,'') and lget (data ,2,'') == 'True' and str (lget (data ,0,'')) == '1.1'  and str (data[11]) == 'True' and imode == 0 ) :

                smsg = 'سلام چطوری ؟ اینم از پنج تای امروزت'
                ooo = read_to_send(id)

            elif str(data [0]) == '4.7' and imode == 1   :

                smsg = 'اینم تا اینجا'
                ooo = read_to_send(id)

        

        if ooo != 0 :

            print ('send start')


            for rrr  in range(1,6) :
                
                q = ooo[rrr-1]
                
                
                
                l = inl[rrr-1]


                
                if str(data [0]) == '5.2' or str(data [0]) == '1.1' :
                
                    db.execute('update user set word%s="%s" , word%i="False" , tday="False"  where   id="%s"' %(l,q[1],int(l)+5,id))
                    sql.commit()
                    smsg += '\n%i_%s' %(rrr  , q[0])
                
                elif str(data [0]) == '4.7':

                    if data[rrr + 3] ==  "Completed!!" :

                        smsg += '\n%i_%s (Completed!!)' %(rrr  , q[0])
                    else :

                        smsg += '\n%i_%s' %(rrr , q[0])


            smsg += "\nدور: %i" %(data[12]+1)
            osend ({'type':'TEXT','body':smsg,'to':id})

            db.execute('update  user set flo="1.3" , mode="wait" ,tday="False" where id="%s"' %id )
            sql.commit()
            print ('sended')
    




