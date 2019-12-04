


from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import _thread
Server="192.168.1.181"
Client_ID="Esp32"
buton1=Pin(19,Pin.IN)
buton2=Pin(21,Pin.IN)
led2=Pin(23,Pin.OUT,value=0)
led1=Pin(22,Pin.OUT,value=0)
count=0

client = MQTTClient(Client_ID, Server)
client.connect()

def buton1_func():
  while True:
    if buton1.value()==1:
      led1.value(buton1.value())
      msg1= "Buton1 durum : {}".format(str(buton1.value()))
      client.publish("test",msg1)
      print(msg1)
    if buton1.value()==0:
      led1.value(buton1.value())
      msg1= "Buton1 durum : {}".format(str(buton1.value()))
      #client.publish("test",msg1)
      #led1.value(not led1.value())
    sleep(0.01)
 
def buton2_func():
  while True:
    if buton2.value()==1:
      led2.value(buton2.value())
      msg2= "Buton2 durum : {}".format(str(buton2.value()))
      client.publish("test",msg2)
      print(msg2)
    if buton2.value()==0:
      led2.value(buton2.value())
      msg2= "Buton2 durum : {}".format(str(buton2.value()))
      #client.publish("test",msg2)
      #led2.value(not led2.value())
    sleep(0.01)

_thread.start_new_thread(buton1_func, ())
_thread.start_new_thread(buton2_func, ())

while True:
  sleep(0.5)






