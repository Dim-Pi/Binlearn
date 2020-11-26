from sys import path 
path.append ('..')

from core import massage 
from user import user
from connect import send_message as send
from list import b_dict as b_list




def uupdate (seter) :
    from core import ulist as uuu
    b_list ( uuu  ,seter)
    return uuu





ulist0 = dict ()
uupdate(ulist0)

#for q in ulist0 :
#    send ({'to':q,'type':'TEXT','keyboard':[] })



for id ,text in massage():

    uupdate(ulist0)
   


