from sys import path
from connect import massages , send_message
from user import user
from mode import mode as md 
#from library import b_user








def b_user (id,msg,lis):


    
    
    if not ( id in user.users() ) :
        lis[id] = user(id,'')
        lis[id].add_user ('')
        #userlis[id] = user (id)
        
        


    ituser = lis [id]

    
    if ituser.name == '' and ituser.mode == '0':
        ituser.smode('name')
    
    
    if ituser.mode  == 'name2' :
        ituser.set_name (msg)
        ituser.smode  ('start')
        


    if ituser.mode == 'name' :

        send_message ({"to":id,"type":"TEXT","body":"واقعا بابت تصمیمت خوشحال شدم(گرچه زحمتش با منه;)\nراستی اسمتو نگفتی!؟"})
        ituser.smode('name2')


    
 




def get_users(lis ):
    for q in user.users() :
        lis[q] = user (q,user.users() [q] ['name'])







ulist = {}

get_users(ulist )




def massage ():



    for input in massages():

        b_user (input ['from']  ,input ['body'] ,ulist)
        #print (str(input) + ulist [input ['from']].name)

        yield ((input ['from']  ,input ['body']))

    


eee = 0




