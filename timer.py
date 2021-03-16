from sys import path 
 
from time import sleep


from library import cnow
from timerdef import timerdef



time_to_sleep = 1



def gen ():
    while True :
        sleep (time_to_sleep)
        yield  1




for now in gen():

    timerdef ()






