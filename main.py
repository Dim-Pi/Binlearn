from sys import path 
from core import massage 
from user import user
from connect import send_message
from list import b_dict as b_list




def uupdate (seter) :
    from core import ulist as uuu
    b_list ( uuu  ,seter)
    return uuu


def barr (id , text) :
    ulist0 = {}
    uupdate(ulist0)
    it = ulist0 [id]
    imode = it.mode
         # select box
    if imode == 'start':
        sen = "عالی شد %s (اسمتو درست گفتم؟) خب حالا بیا شروع کنیم " %it.name
        send_message ({"to":id,"type":"TEXT","body":sen})
        it.smode('start2')











ulist0 = dict ()
uupdate(ulist0)



for id ,text in massage():

    uupdate(ulist0)
    print ("%s: %s" %(ulist0[id].name,text))
    barr (id,text)


