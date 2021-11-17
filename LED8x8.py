import time
from shifter import Shifter    # extend by composition
import multiprocessing
import random

class LED8x8(multiprocessing.Process): #declares LED8x8 as a multiprocessing clas
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock) #sends data latch and clock pins to shifter class
    a = multiprocessing.Array('i',8) #sets a to be a 8 value array
    ay = 5 #sets ay to initially be 5
    ax = 5 #sets ax to initially be 5
    g = 0b1 #sets g to initally be 1 
    mask = 0b11111111  #creates bit mask
    while True:
      h = 0 #sets h to initially be 0
      while h == 0: #runs while h = 0
        x = random.randint(-1, 1) #sets x to be a random number between -1 and 1
        y = random.randint(-1, 1) #sets y to be a random number between -1 and 1
        ax += x #increases ax by x
        ay += y #increases ay by y
        if ax >= 1: #checks that ax is on
          if ax <= 8:
            if ay >= 1:
              if ay <= 8:
                h = 1
        else:
          h = 0
          ax -= x
          ay -= y
      f = g << abs(8-ax)
      e = ~f & mask
      a[ay] = e
      self.p = multiprocessing.Process(name='myname', target = self.display(ay, a), args = (ay, a))
      self.p.daemon = True
      self.p.start()
      time.sleep(0.1)
  def display(self, num, c):
    self.shifter.shiftByte(c[num])
    self.shifter.shiftByte(1 << (num))
