

from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import _thread
Server="192.168.1.172"
Client_ID="Esp32"
topic="buton1"
topic2="buton2"
buton1=Pin(19,Pin.IN)
buton2=Pin(21,Pin.IN)
led2=Pin(23,Pin.OUT,value=0)
led1=Pin(22,Pin.OUT,value=0)
count=0
def sub_cb(topic, msg):
  message=msg.decode()
  d_topic=topic.decode()
  print((d_topic,message))
  if message == "ON" and d_topic=='buton1':
    led1.value(1)
    msg1= "Buton1 durum : {}".format(str(led1.value()))
    client.publish(topic,msg1)
    print(msg1)
  if message == "OFF" and d_topic=='buton1':
    led1.value(0)
    msg1= "Buton1 durum : {}".format(str(led1.value()))
    client.publish(topic,msg1)
    print(msg1)
  if message == "ON" and d_topic=='buton2':
    led2.value(1)
    msg2= "Buton2 durum : {}".format(str(led2.value()))
    client.publish(topic2,msg2)
  if message == "OFF" and d_topic=='buton2':
    led2.value(0)
    msg2= "Buton2 durum : {}".format(str(led2.value()))
    client.publish(topic2,msg2)

client = MQTTClient(Client_ID, Server)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic)
client.subscribe(topic2)

def buton1_func():
  while True:
    if buton1.value()==1:
      flag1=1
      while buton1.value()==1:
        pass
    else:
      flag1=0
      msg1= "Buton1 durum : {}".format(str(led1.value()))
      #client.publish(topic,msg1)
      while buton1.value()==0:
        pass
    if flag1==1:
      led1.value(not led1.value())
      msg1= "Buton1 durum : {}".format(str(led1.value()))
      client.publish(topic,msg1)
  
def buton2_func():
  while True:
    if buton2.value()==1:
      flag2=1
      while buton2.value()==1:
        pass
    else:
      flag2=0
      msg2= "Buton2 durum : {}".format(str(led2.value()))
      #client.publish(topic,msg1)
      while buton2.value()==0:
        pass
    if flag2==1:
      led2.value(not led2.value())
      msg2= "Buton2 durum : {}".format(str(led2.value()))
      client.publish(topic2,msg2)
      
      
  
_thread.start_new_thread(buton1_func, ())
_thread.start_new_thread(buton2_func, ())

def subscribe():
  while True:
    new_message = client.check_msg()
    if (new_message != 'None'):
      pass
    sleep(0.0001)

_thread.start_new_thread(subscribe, ())












