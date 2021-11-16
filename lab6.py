import time
from LED8x8 import LED8x8
from LED8x8Copy import LED8x8Copy
import multiprocessing
import random

dataPin, latchPin, clockPin = 13, 19, 26

#LED= LED8x8(dataPin, latchPin, clockPin)
ay = 5
ax = 5
g = 0b1
mask = 0b11111111

while True:
  try:
    h = 0
    while h == 0:
      x = random.randint(-1, 1)
      y = random.randint(-1, 1)
      ax += x
      ay += y
      if ax >= 0:
        if ax <= 7:
          if ay >= 0:
            if ay <= 7:
              h = 1
      else:
        h = 0
        ax -= x
        ay -= y
    f = g << abs(7-ax)
    e = ~f & mask
    a = multiprocessing.Array('i',8)
    a[ay] = e
    #p = LED8x8Copy(dataPin,latchPin,clockPin, ay, a)
    LED = LED8x8Copy(dataPin, latchPin, clockPin, ay, a)
    #p = multiprocessing.Process(name='myname',target=LED.display(ay, a),args=(ay, a))
    #p.daemon = True
    #p.start()
    #time.sleep(0.1)
    ##
  except Exception as e:   # catch everything, just in case
    print(e)               # delete once code is debugged
    LED.p.terminate()      # terminate the process
    LED.p.join(2)          # wait up to 2 sec for process