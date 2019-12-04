




#This file is executed on every boot (including wake-boot from deepsleep)
import esp
import network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("Votec", "Vb.142536")
print(station.isconnected())
station.ifconfig()
from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import _thread 








