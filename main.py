from machine import Pin
from time import sleep

l1 = Pin (1, Pin.OUT)
l2 = Pin (2, Pin.OUT)
b1 = Pin (27, Pin.IN)
b2 = Pin (28, Pin.IN)
X = 13

while X == 13:
  if b1.value():
    l1.on()
  if l1.value():
    l1.off()

  if b2.value():
    if l2.value() == 1:
      l2.off()
    elif l2.value() == 0:
      l2.on()

    sleep(.5)
    