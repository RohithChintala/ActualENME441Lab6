import time
from shifter import Shifter    # extend by composition
import multiprocessing
import random

class LED8x8Copy(multiprocessing.Process):
  def __init__(self, data, latch, clock):
    #multiprocessing.Process.__init__(self)
    self.shifter = Shifter(data, latch, clock)
    self.b = multiprocessing.Array('i',8)
    self.d = multiprocessing.Value('i')
    #self.b[num] = a
    #multiprocessing.Process.__init__(self, target=self.display(num,a), args= (num, a))
    #self.p = multiprocessing.Process(name='myname', target = self.display(num, self.b), args = (num, self.b))
    self.p = multiprocessing.Process(name='myname', target = self.display(self.d, self.b), args = (self.d, self.b))
    self.p.daemon = True
    self.p.start()
    ay = 5
    ax = 5
    g = 0b1
    mask = 0b11111111 
    while True:
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
      self.b[ay] = e
      self.d = ay
      time.sleep(0.1)
    #self.p.join()
    #while True:
      #self.display(num, a)
      #self.b = multiprocessing.Array('i',8)
      #self.b[num] = a[num]
      #self.p = multiprocessing.Process(name='myname', target = self.display(num, a), args = (num, a))
      #self.p.daemon = True
      #self.p.join()
  def display(self, num, c):
    while True:
      self.shifter.shiftByte(c[num.value])
      self.shifter.shiftByte(1 << (num.value))
