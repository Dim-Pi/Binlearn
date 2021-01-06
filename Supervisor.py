from sys import path , argv
from core3 import admn_send as asend  
from subprocess import call
from platform import system as si
import os 



ba = {'Windows':'\\','Linux':r'/'}
b = ba[si()]

print (argv[0])
os.chdir(os.path.dirname(os.getcwd() + b + argv [0]))


print (os.getcwd())
s = os.getcwd()
print (s) 
my = s.split(b)
print (my)
loc =  b.join(my)
print (loc)


File = r'admin_client'
pypro = loc + b + File + r'.py'


while True :

    try :
        print ('Supervisor is starting server .......')
        print ('%s......\n\n'%pypro)
        call ('python3 %s' %pypro)

    except Exception as e :
        print ('start filed!')
        try:
            print ('start sql.....\n\n')
            call ('systemctl start mariadb')
        except :
            pass
        asend (e)
        continue
















