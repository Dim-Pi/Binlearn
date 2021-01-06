from sys import path , argv
from core3 import admn_send as asend  
from subprocess import call
from platform import system as si
import os 

print (argv [0])
os.chdir(os.path.dirname(argv [0]))


ba = {'Windows':'\\','Linux':r'/'}
b = ba[si()]

print (os.getcwd())
s = os.getcwd()
print (s)
my = s.split(b)
print (my)
loc =  b.join(my)
print (loc)


File = r'timer'
pypro = loc + b + File + r'.py'


while True :
    try :
        print ('Supervisor is starting timer .......\n\n')
        call ('python3 %s' %pypro)
    except Exception as e :
        print ('start filed!')
        asend (e)
        continue
        
















