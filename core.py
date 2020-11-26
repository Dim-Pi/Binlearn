
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
    imd = ituser.mode
    
    if ituser.name == '' and ituser.mode == '0':
        ituser.smode('name')
    
    
    elif ituser.mode  == 'name2' :
        ituser.set_name (msg)
        ituser.smode  ('name3')
    
    elif imd == 'rename2':
        ituser.set_name (msg)
        ituser.smode ('rename3')

    elif ituser.mode == 'name' :

        send_message ({"to":id,"type":"TEXT","body":"واقعا بابت تصمیمت خوشحال شدم(گرچه همه زحمتا با منه;)\nراستی اسمتو نگفتی!؟"})
        ituser.smode('name2')


    
 







def barr (id , text ,ulist) :
    
    it = ulist [id]
    imode = it.mode
         # select box

    if imode == 'name4' :

        if text == 'False':
            sen = "شرمنده): حالا زحمتت یه بار بگو باید بیشتر حواسمو جمع کنم"
            it.smode ('rename2')
        elif text == 'True':
            send_message ({'body':'خب خدا رو شکر' ,'type' : 'TEXT' , 'to': id  })
            sen = "راستی کلماتی که من بلدم معمولا معنیاشون اشتباست اگه اشتباه بود درستشون رو برام بفرست"
            it.smode ('start')
        else :
            sen = 'جان؟؟؟'
        

        send_message ({'type':'TEXT','body':sen,'to':id})


    elif imode == 'rename4' :

        if text == 'False':
            sen = "کم کم دارم احساس میکنم که مشکل از من نیست(:\n یا سر کارم گذاشتی!!!"
            send_message ({'type':'TEXT','body':sen,'to':id})
            sen = 'حالا عیب نداره یه بار دیگه اسمتو بگو'
            it.smode ('rename2')
        elif text == 'True':
            send_message ({'body':'خب خدا رو شکر' ,'type' : 'TEXT' , 'to': id  })
            sen = "راستی کلماتی که من بلدم معمولا معنیاشون اشتباست اگه اشتباه بود درستشون رو برام بفرست"
            it.smode ('start')
        else :
            sen = 'جان؟؟؟'
    
        send_message ({'type':'TEXT','body':sen,'to':id})




    elif imode == 'name3':
        
        key =  [[{'command':'True','text':'آره درسته'},{'text':'نه بابا اشتباه شد','command':'False'}]]
        sen = "عالی شد ،%s (اسمتو درست گفتم؟) خب حالا بیا شروع کنیم " %it.name
       
     
        

        send_message ({"to":id,"type":"TEXT","body":sen , "keyboard":key})
        it.smode('name4')

    elif imode == 'rename3':
        sen = 'امیدوارم این دفعه اشتباه نشده باشه خب بزار.........\n اسمت %s شد دیگه درسنه؟' %it.name
        key =  [[{'text':'مثل اینکه دوباره اشتباه شده!!!','command':'False'},{'command':'True','text':'خدارو شکر درسته'}]]
        send_message ({"to":id,"type":"TEXT","body":sen , "keyboard":key})
        it.smode ('rename4')




def get_users(ulist):
    for q in user.users() :
        ulist[q] = user (q,user.users() [q] ['name'])







ulist = {}

get_users(ulist)




def massage ():



    for input in massages():

        
        

        b_user (input ['from']  ,input ['body'] ,ulist)
        barr (input ['from']  ,input ['body'] ,ulist)
        #print (str(input) + ulist [input ['from']].name)

        yield ((input ['from']  ,input ['body']))

    


eee = 0




