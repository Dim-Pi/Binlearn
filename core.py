from sys import path

path.append('..')


from client import Client
from library import convertpe , convertep
from user import user 





bot_token = 'WHPulnGQWSGB8zSaKT31ARIeE4iJdfs-TkT-O4itKkwOp9iCJGxenVF7A2PIsqk37XLvYC728J1eG08WVVwK9HfnAudfGl3YF899eG86LX_mqYIC5MdzFVJBTsXmS0W417_5MQaKZhKklfHg'

bot1 = Client(bot_token)
bot1.RETRY_DELAY = 1

def massages ():

   try:
      messages = bot1.get_messages()
      for msg in messages: 

         msg ['body'] = convertpe (msg ['body'])
         print ("(receive)   %s: %s "  %(user.get_id(msg['from']),msg['body']))
         
         yield (msg)

   except Exception as e:
      print(e.args[0])



 
 
def esend (text ,id):
   
   send_message ({"to":id,"type":"TEXT","body": str(text)})


def send_message (data0):

   data = {'to':data0['to'] , 'type' : 'TEXT' , 'body' : data0.get('body','') , 'keyboard':data0.get ('keyboard',[]) }

   print ('(send)      %s: %s '% (user.get_id(data['to']) ,data['body']) )
   bot1.send_message ( data )














#url = "https://bot.sapp.ir/XayO8FeO8PDjV1Xq0unWmLxsUf6MjFMnG5DFk7EVwRTsSD4PVc8lMX-d3AlBqu6e4zbLWIioqyMb_nwr1vmVMeUy3c3x_ZWZBoBjKQF6H3QcHUdkKfe2LDUTwcvl8ZDBI8NYkOGD8dTUdBqm/getMessage"
