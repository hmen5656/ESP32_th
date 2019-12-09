from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import _thread
Server="192.168.1.181"
Client_ID="Esp32"
buton1=Pin(19,Pin.IN)
buton2=Pin(22,Pin.IN)
led2=Pin(23,Pin.OUT,value=0)
led1=Pin(18,Pin.OUT,value=0)
count=0
def buton1_func():
  while True:
    led1.value(not led1.value())
    sleep(0.5)
    led1.value(not led1.value())
    sleep(0.5)
  
  

 
def buton2_func():
  while True:
    led2.value(not led2.value())
    sleep(0.8)
    led2.value(not led2.value())
    sleep(0.8)
  
#_thread.start_new_thread(buton1_func, ())
#_thread.start_new_thread(buton2_func, ())

if __name__ == '__main__':
  buton1_func()
  buton2_func()
