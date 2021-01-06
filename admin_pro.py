from sys import path 
from core import send_message as esend 
from atoken import inlearn
from library import convertep as cep 
dmn = inlearn.dmn


def uselkey (udic) :

    di = list()
    di0 = [[]]
    num0 = int()
    num1 = int()

    for use0 in udic :

        use = udic [use0]
        di.append ({'id':use.id , 'na':use.name})
    
    for q in di :

        num0 += 1
        di0[num1].append ({"text":cep(q['na']) ,"command":q['id'] })
        if num0 == 3 :
            num0 = 0
            num1 += 1
            di0.append([])

    di0.append([{'text':'بیخیال','command':'//FALSE'}])
  
    return di0












def admin2 (udic):

    
    admn = udic [dmn()]
    Fkey = {'text':'بازگشت','command':'//FALSE'}

    if admn.lmsg == "//FALSE":

        admn.wait()

    elif admn.mode == 'admin0':

        try :
            admn.adminu = udic[admn.lmsg]
            this = admn.adminu
            this.atsync()
            sm = "چیکارش کنم؟"
            if admn.adminu.mode == 'block':
                key = [[{'text':'Unlock','command':'//block'}]]
            else:
                key = [[{'text':'block','command':'//block'}]]
        
            key[0].append ({'text':'delete','command':'//Delete'})
            key.append ([{'text':'بریم یه گپی بزنیم','command':'//Gap'}])


            key.append ([Fkey])

            sm += ('\n دور : %i' %this.modint )






            admn.send ({'body':sm,'keyboard':key})
            admn.smode  ("admin1")

        except:

            admn.send ({'body':'','keyboard':[[Fkey]]})





    elif admn.mode == 'admin1':

        fun = dict()
        fun['//block']   =  lambda it , udic , adm : it.block()
        fun['//Delete']  =  dell0
        fun['//Gap']     =  gap 

        it = admn.adminu
        try:
            fun[admn.lmsg] (it)
        except :

            try:
                fun[admn.lmsg] (it,udic,admn) 
            except :
                pass
        if not admn.lmsg in ['//Gap'] :
            key = uselkey (udic)
            admn.send ({'body':'','keyboard':key})
            admn.smode ( "admin0" )

    else :
        
        key = uselkey (udic)
        admn.send ({'body':'','keyboard':key})
        admn.smode ("admin0")






def dell0 (it,udic,admn) :
    
    del (udic[it.id])
    it.remove()

def gap (use,ud,adm):

    adm.lmod = adm.mode
    use.lmod = use.mode
    adm.smode('chat')
    use.smode('chat')
    adm.chat = use.id
    use.chat = adm.id  





