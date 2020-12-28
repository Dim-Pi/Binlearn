from re import search , findall , sub
from sys import path
from start_client import input_msg
from core import send_message as osend
from words import mianword
from list import b_dict , list_get
from library import convertep as convert
from library import cnow
import words
from timerdef import timerdef





def uupdate (seter) :
    from user_client import ulist as uuu
    b_dict ( uuu  ,seter)
    return uuu


























def   chk_next (it) :

    if it.chek_complet() :

        if it.mode != 'next' :

            it.comeat({'mode':'next','sendtime':cnow(),'flo':1.3})

            sm = "خب مثل اینکه این قسمت تموم شد \n حالا چیکار کنیم؟"
            key = [[{'text':"بریم قسمت بعد",'command':'//True'},{'text':"فعلا حوصله ندارم فردا بفرست",'command':'//False'}]]
            it.send ({'body':sm , 'keyboard':key})

        elif it.mode == 'next' :

            if it.lmsg == '//True':

                it.next ()
                it.wait ()
            elif it.lmsg == '//False':

                it.next ()
                it.comeat ({'mode':'wait' , 'flo':1.1 , 'sendtime':cnow()})












def edit (id ,msg) :
    





    it = udict [id]
    imd = it.mode
    keyF0 = [[{'text':'کامل و درست','command':'//True'},{'text':'کلا اشتباهه','command':'//False'}],[{'text':'درسته ولی میشه معنی های بیشتری براش نوشت','command':'//Frue'},{'text':'بی خیال پشیمون شدم','command':'//FALSE'}]]

    if imd[4] == 'F':                                                                          # _______
                                                                                               #|
        itw = it.modeed                                                                        #| 
                                                                                               #|_______
        if imd[5] == '0':                                                                      #|
                                                                                               #|
                                                                                               #|  
            sm = 'بررسی کن این درسته یا نه\n%s :     %s' %(itw.en,itw.fa)        
            osend ({'body':sm,'type':'TEXT','to':id,'keyboard':keyF0})

            it.smodeed(itw)

        elif imd[5] == '1':

        

            sm = 'پس زحمتت درستشو بفرست(فقط معنی فارسی ؛اگر چندتا معنی داره بینشون با( ، یا ,) فاصله بزار)'

            osend ({'type':'TEXT','to':id,'body':sm})

            sm = 'در ضمن ارسال چیزی که اشتباه باشه اشکال شرعی داره'

            osend ({'type':'TEXT','body':sm,'to':id,'keyboard':[[{'text':'بی خیال',"command":"//FALSE"}]]})
            it.smode ('editF2')
        




        elif imd[5] == '2':
            
            lw = it.modeed

            newf = sub ('(،)',',',msg)

            im = lw.edit(newf)
            it.sync()

            if im == True :

                osend ({'type':'TEXT',"to":id,'body':"ممنون از کمکت"})
                it.wait()
            else :

                osend ({'type':'TEXT',"to":id,'body':"نفهمیدم چی شد ولی یک ارور مهکم خورد تو سرم!!"})
                it.wait()
                
            
            chk_next (it)




        elif imd[5] == '3':

            sm = "خب پس لطفا ترجمه هایی که میتونن اضافه شن رو ارسال کن(اگر بیشتر از یکی ان با ، یا , بینشون فاصله بزار)"            
            osend ({'type':'TEXT','body':sm,'to':id,'keyboard':[[{'text':'بی خیال',"command":"//FALSE"}]]})
            it.smode ('editF4')






        elif imd[5] == '4' :
            

            lw = it.modeed

            newf = sub ('(،)',',',msg)

            im = lw.add_fa(newf)
            it.sync()

            if im == True :

                osend ({'type':'TEXT',"to":id,'body':"ممنون از کمکت"})
                


            else :

                osend ({'type':'TEXT',"to":id,'body':"نفهمیدم چی شد ولی یه هو یک ارور مهکم خورد تو سرم!!"})
                

            if it.chek_complet() :
                chk_next (it)
            else:
                it.wait()










    elif imd[4] == 'B' :                                    # _______
                                                            # |      \ 
                                                            # |       |
        itw = it.editmode()                                 # |______/
                                                            # |      \
        if imd[5] == '0':                                   # |       |
                                                            # |       |
            keyB0 = [[]]                                    # |______/

            sm = 'هرکدوم اشتباهه بگو:\n\n\n'
            ad = 1
            wt = int()

            b = 1



            for q in it.words():

                wt += len(q.en)

                sm += "%i_%s :   %s\n"%(ad,q.en,q.fa)
                ad += 1



            if wt >= 2:
                b = 1
                keyB0.append([])


            ooolis = []

            o = 0

            for q in it.words():
                ooolis.append (q)

            for q in ooolis [:3]:

                keyB0[0].append({'text':q.en,'command':'//b/%i'%q.num})
                o += 1

            for q in ooolis [3:] :
                keyB0[b].append({'text':q.en,'command':'//b/%i'%q.num})
                o += 1



            keyB0.append([{'command':'//FALSE','text':'ولش کن دکمه غلط کردمش کجاست؟'}])



            osend ({'body':sm,'type':'TEXT','to':id,'keyboard':keyB0})


         
        elif imd[5] == '1':


            edw = awords [int(msg)] 

            sm = 'هر جاش اشتباهه بگو\n%s :     %s' %(edw.en,edw.fa)        
            osend ({'body':sm,'type':'TEXT','to':id,'keyboard':keyF0})

            it.smode("editB2")
            it.smodeed(edw)


        elif imd[5] == '3':

        

            sm = 'پس زحمتت درستشو بفرست(فقط معنی فارسی ؛اگر چندتا معنی داره بینشون با( ، یا ,) فاصله بزار)'

            osend ({'type':'TEXT','to':id,'body':sm})

            sm = 'در ضمن ارسال چیزی که اشتباه باشه اشکال شرعی داره'

            osend ({'type':'TEXT','body':sm,'to':id,'keyboard':[[{'text':'بی خیال',"command":"//FALSE"}]]})
            it.smode ('editB5')
        



        elif imd[5] == '5':


          
            lw = it.modeed

            newf = sub ('(،)',',',msg)

            im = lw.edit(newf)
            it.sync()


            if im == True :

                osend ({'type':'TEXT',"to":id,'body':"ممنون از کمکت"})
                it.wait()
            else :

                osend ({'type':'TEXT',"to":id,'body':"نفهمیدم چی شد ولی یک ارور مهکم خورد تو سرم!!"})
                it.wait()


            chk_next (it)


        elif imd[5] == '4':

            
            sm = "خب پس لطفا ترجمه هایی که میتونن اضافه شن رو ارسال کن(اگر بیشتر از یکی ان با ، یا , بینشون فاصله بزار)"            
            osend ({'type':'TEXT','body':sm,'to':id,'keyboard':[[{'text':'بی خیال',"command":"//FALSE"}]]})
            it.smode ('editB6')





        elif imd[5] == '6' :


            lw = it.modeed

            newf = sub ('(،)',',',msg)


            im = lw.add_fa(newf)
            it.sync()



            if im == True :

                osend ({'type':'TEXT',"to":id,'body':"ممنون از کمکت"})
                it.wait()
            else :

                osend ({'type':'TEXT',"to":id,'body':"نفهمیدم چی شد ولی یه هو یک ارور مهکم خورد تو سرم!!"})
                it.wait()


            chk_next (it)




            






















def expert (text):
    msg2 = text.split(',')
    if search(r'\d',msg2[0]) == None :

        if search(r'\d',list_get(msg2,1,None)) == None :
            osend ({'type':'TEXT','body':'جان؟؟؟','to':id})
        else :
            dig = findall(r',(\d)',msg2[1])
            lis = findall (r',(\w+)',',%s'%msg2[0])

    else:
        dig = findall(r'(\d),',msg[0])
        lis = findall (r',(\w+)',',%s'%msg2[1])

    return {dig[0]:lis}

















def chek (id ,msg):

    from time import sleep

    if len(msg) < 4 :

        msg = '0o35fgllfclkfi'


    it = udict[id]
    imd = it.mode

    key01 = [[{'text':'نه بابا کار دارم','command':'//FALSE'},{'command':'//True','text':'چطوری کمکت کنم؟'}]]
    ms = 'آفرین احسنت کاملا درسته'
    fms2 = lambda en ,fa : '%s :\n%s' %( en ,fa )
    eee = 0

    while eee == 0 :
        try :

            
            it.sync()
            it.wsync()
            fawor = it.get_words()
            if type (fawor)  ==  list :
                fawor =  fawor [0]
            else :
                fawor = []
                chk_next (it)

            eee = 1

        except Exception as e:
            
            sleep (1)
            eee = 0
            continue

    ad = 0
    aa = 0
    ao = 0
    aw = ''

    for q in fawor :

        aa += 1

        eeee = words.find_num(q)[0]
        print ('errrrrorrrr') 



        itw = awords [eeee]

        mw = mianword (q)

        if type(q) == list :

            q = ','.join(q)

        q1 = convert (q)
        msg1 = convert (msg)



        if itw.mode  == 'True' :

            if msg1 in q1.split(',') :
                ad += 100
                ao = str(aa)
                aw = itw
                
                break 

        elif itw.mode == 'False' :

            if (msg1 == q1) or (msg1 in q1) :
                ad += 1
                ao = str(aa)
                aw = itw
                
                break



    if ad == 1 :

        osend ({'body':ms , 'type':'TEXT' , 'to' : id , 'keyboard' : []})
        it.comeat ({'mode':'//editF' , 'word%i'%(int(ao)+5):'True'})
        it.smodeed ( aw )

        ms2 = 'زحمتت میتونی یه کمکی بکنی؟؟'
        osend ({'body':ms2 ,'type':'TEXT' ,'to':id ,'keyboard':key01})
        it.okword(ao)


    elif ad == 100 : 

    
        ms5 = 'دمت گرم بابا'
        it.okword(ao)
        it.send({'body':ms5})
        it.wait()
        chk_next (it)


    elif ad == 0 :

        ms8 = 'به نظرم یه اشتباه تایپی کردی یا یه همچین چیزی حالا با دقت بیشتر دوباره امتحان کن'
        osend ({'body':ms8,'type':'TEXT','to':id,'keyboard':[[{'text':'به نظرم اشتباه از خودته و معنی کلمات رو درست بلد نیستی!' ,'command':r'//editB'}]]})
        it.smodeed (str(ao))
























def code (id ,msg):

    it = udict[id]




    if msg == '//FALSE':
        if it.chek_complet() :
            chk_next(it)
        else :
            it.wait()
        


    elif search (r"//(\w/.)",msg) != None:

        mcd = findall  (r"//(\w/.{1,3})",msg) [0]
        cd = mcd.split(r'/')
        if cd[0] == 'b':
            it.smode('editB1')
            edit (id ,cd[1])

    elif msg == '//editB':
                
        it.smode('editB0')
        edit (id ,msg)
 
    elif it.mode [:5] == 'editB':

        if it.mode == 'editB0':
            if msg == 'False':
                it.smode ('wait')
            else :
                it.smode ('editB1')
                edit (id ,msg)



        elif it.mode [5] == '2':


            if msg == '//True':
                try :
                    it.modeed.save()
                    
                except :
                    it.wait()
                it.send ({'body':'دمت گررررم'})
                it.wait()
                chk_next (it)
          
            elif msg == '//False':
                it.smode('editB3')
                edit (id ,msg)
            elif msg == '//Frue':
                it.smode('editB4')
                edit (id ,msg)







    elif it.mode [:5] == 'editF':


        if  it.mode [5] == '0':
    
            if msg == '//False':
                it.smode ('editF1')
                edit (id ,msg)
            elif msg == '//Frue' :
                it.smode ('editF3')
                edit (id ,msg)
            elif msg == '//True' :
                it.word_save()
                it.send({'body':'ممنونم'})
                it.wait()


    elif it.mode == 'next' :

        chk_next (it)









    elif it.mode == '//editF' :


        if msg == '//True' :

            it.smode('editF0')
            edit (id ,msg)
        
        elif msg == '//False' :

            it.smode('wait')


    elif it.mode == 'editF0' :

        if msg == 'True':

            itw = it.modeed
            itw.save()







awords = dict()
awords = words.words()

udict = dict()
uupdate(udict)






for id , msg in input_msg() :

    uupdate (udict)
    print ('Ok!!\n')
    
    udict[id].lmsg = msg 
    
    if udict[id].mode == 'wait0':
        udict[id].smode('wait')
        
    if udict[id].ready == 'True':
        if '//' not in msg :
            if 'edit' in udict[id].mode  :
                edit (id ,msg)
            elif 'wait' == udict[id].mode :
                chek (id ,msg)
        else :
            code (id ,msg)
















