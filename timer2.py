from sys import path
from core2 import send_message as osend
from words import lwords 
from atoken import DBInformation as DBI
from mysql.connector import connect
from re import findall
from time import sleep , localtime









sql = connect (
    user = DBI.usr(),
    password = DBI.pas(),
    database = DBI.dbn()
)



db = sql.cursor()





print ('connected')




def gen ():
    while True :
        sleep (5)
        yield  list(localtime() ) [3]









def extract (qmode):



    lw = list()

    lqm = findall ( '(\d+)<>' , qmode )

    alw = dict()

    for q0 in lqm :

        q = lw [q0]

        alw [q.en] = q.fa.split(',')


    return alw












for q in gen() :



    sql = connect (
        user = DBI.usr(),
        password = DBI.pas(),
        database = DBI.dbn()
    )


    db = sql.cursor()

    db.execut ('select id ,qmode from user')


    try:
        
        lusers = db.fetchall()
    
    

        

        for user in lusers :

            id = user [0]

            if user [1] != '<>':
                words = extract(user[1])



    except :

        continue












































