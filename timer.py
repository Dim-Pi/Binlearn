from sys import path 
 
from time import sleep


from library import cnow
from timerdef import timerdef







def gen ():
    while True :
        sleep (5)
        yield  1




for now in gen():

    timerdef ()






