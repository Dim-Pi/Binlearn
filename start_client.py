from sys import path 
path.append ('..')

from user_client import massage 
from user import user
from core import esend 
from core import send_message as osend
from list import b_dict as b_list
from library import give_data as give



def uupdate (seter) :
    from user_client import ulist as uuu
    b_list ( uuu  ,seter)
    return uuu


def exam (it,msg):

    
    imd = it.mode
    id = it.id

    send = lambda txt : esend (txt,id)

    key1 = [[{'text':'نه بابا آماده نیستم','command':'False'},{'text':'فکر می کنم که آماده ام','command':'Frue'},{'text':'صد در صد','command':'True'}]]

    if imd == 'start':

        smsg =  '''خب ببین ساز و کار اینجوریه که هر روز صبح من پنج تا کلمه انگلیسی برات میفرستم بعد شما هم لطف میکنی و تا آخر روز معادل فارسی شون رو ارسال میکنی 
        همین!!
        به همین سادگی ''' 
        
        
        
        send (smsg)

        
        smsg = {'type':'TEXT', 'to':id , 'keyboard' : key1 , 'body':'اگه آماده ای که شروع کنیم؟'}
        osend (smsg)

        it.comeat({'mode':'start2'})

    elif imd == 'start2':

        if msg == 'True':
            send ('عالیه')
            it.comeat({'mode':'wait','ready':'True','flo':5.2,'modint':0})
        elif msg == 'False':
            send ('(:(:مهم نیست:):)')
            it.comeat({'mode':'wait','ready':'True','flo':5.2,'modint':0})
        elif msg == 'Frue':
            send ('نظر منم همینه')
            it.comeat({'mode':'wait','ready':'True','flo':5.2,'modint':0})
        else:
            osend ({'body':'جان؟؟','type':'text','to':id,'keyboard':key1,})
    










def driver (it ,msg):

    imd = it.mode

    if 'name' not in imd :
        exam (it ,msg)








ulist0 = dict ()
uupdate(ulist0)

#for q in ulist0 :
#    send ({'to':q,'type':'TEXT','keyboard':[] })


def input_msg ():

    for id ,text in massage():

        uupdate(ulist0)

        it = ulist0 [id]

        driver (it ,text)

        yield (id , text)

   





