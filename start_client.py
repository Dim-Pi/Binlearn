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
            ystart (it)
        elif msg == 'False':
            send ('(:(:مهم نیست:):)')
            ystart (it)
        elif msg == 'Frue':
            send ('نظر منم همینه')
            ystart (it)
        else:
            osend ({'body':'جان؟؟','type':'text','to':id,'keyboard':key1,})
    



def ystart (it):
    it.comeat({'mode':'wait0','ready':'True','flo':5.2,'modint':0,'qmode':'<.>'})





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
        it = ulist0[id]
        
        if ('name' in it.mode) or ('start' in it.mode) :
      


            driver (it ,text)
        else :
            yield (id , text)

   





