from mysql.connector import connect 
from re import sub
from time import  localtime
from atoken import DBInformation as DBI







def convertpe (text):
    
    
    con_dic = {
    
        'ا' : 'a0a',  'آ' : 'A0a',  'ب' : 'b0b',  'پ' : 'p0p',  'ت' : 't0t',  'ث' : 's0c',
        'ج' : 'j0j',  'چ' : 'c0h',  'ح' : 'H0H',  'خ' : 'k0h',  'د' : 'd0d',  'ذ' : 'z0Z',
        'ر' : 'r0r',  'ز' : 'z0z',  'ژ' : 'z0h',  'س' : 's0s',  'ش' : 's0h',  'ص' : 'S0S',
        'ض' : 'Z0Z',  'ط' : 'T0T',  'ظ' : 'Z0z',  'ع' : 'A0A',  'غ' : 'g0H',  'ف' : 'f0f',
        'ق' : 'g0h',  'ک' : 'c0k',  'گ' : 'g0g',  'ل' : 'l0l',  'م' : 'm0m',  'ن' : 'n0n',
        'و' : 'v0w',  'ه' : 'h0h',  'ی' : 'y0y',  ' ' :  ' ' ,  '،' :  ',' 


    }

    
    newtext = text
    
    

    for q in con_dic:
        newtext = sub ('(%s)' %q,con_dic[q],newtext)



    return newtext







def cnow ():

    return list(localtime() ) [3]





def rsend (tx) :
    return '\n(send)        '.join (tx.splitlines ())


def rrese (tx) :
    return '\n(receive)     '.join (tx.splitlines ())



def signrun ():
    print ('\n\n<0run0>')







def convertep (text):



    con_dic = {



        'a0a': 'ا',  'A0a': 'آ',  'b0b': 'ب',  'p0p': 'پ',  't0t': 'ت',  's0c': 'ث',
        'j0j': 'ج',  'c0h': 'چ',  'H0H': 'ح',  'k0h': 'خ',  'd0d': 'د',  'z0Z': 'ذ',
        'r0r': 'ر',  'z0z': 'ز',  'z0h': 'ژ',  's0s': 'س',  's0h': 'ش',  'S0S': 'ص',
        'Z0Z': 'ض',  'T0T': 'ط',  'Z0z': 'ظ',  'A0A': 'ع',  'g0H': 'غ',  'f0f': 'ف',
        'g0h': 'ق',  'c0k': 'ک',  'g0g': 'گ',  'l0l': 'ل',  'm0m': 'م',  'n0n': 'ن',  
        'v0w': 'و',  'h0h': 'ه',  'y0y': 'ی',   '،' : ',' 



    }

    rtext = text
    for q in con_dic:

        rtext = sub ('(%s)'%q , con_dic[q] ,rtext)

    return rtext
























def b_per (text) :



    con_dic = {
    
        'ا' : 'a0a',  'آ' : 'A0a',  'ب' : 'b0b',  'پ' : 'p0p',  'ت' : 't0t',  'ث' : 's0c',
        'ج' : 'j0j',  'چ' : 'c0h',  'ح' : 'H0H',  'خ' : 'k0h',  'د' : 'd0d',  'ذ' : 'z0Z',
        'ر' : 'r0r',  'ز' : 'z0z',  'ژ' : 'z0h',  'س' : 's0s',  'ش' : 's0h',  'ص' : 'S0S',
        'ض' : 'Z0Z',  'ط' : 'T0T',  'ظ' : 'Z0z',  'ع' : 'A0A',  'غ' : 'g0H',  'ف' : 'f0f',
        'ق' : 'g0h',  'ک' : 'c0k',  'گ' : 'g0g',  'ل' : 'l0l',  'م' : 'm0m',  'ن' : 'n0n',
        'و' : 'v0w',  'ه' : 'h0h',  'ی' : 'y0y',  '،' :  ','


    }

    
    
    u = True

    for q in str(text).strip() :
        if not (q in con_dic) :
            u = False
    

    return u 
            







def gname (id) :
    sql , db = sync()

    db.execute ("SELECT name FROM user WHERE id='%s'" %id)
    try :
        nam = db.fetchall() [0] [0]
        return nam
    except :
        return 'None'
    










def give_data ():
 
    sql , db = sync()

    db.execute('select * from words')
    words = db.fetchall()

    dword = dict()
    for q in words :
        dword[q[0]] = q[1]

    return dword
















def sync(): 
    sql = connect (
        user     =  DBI.usr(),
        password =  DBI.pas(),
        database =  DBI.dbn()

    )

    db = sql.cursor()

    return sql ,db    













