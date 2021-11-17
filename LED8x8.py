import time
from shifter import Shifter    # extend by composition
import multiprocessing
import random

class LED8x8(multiprocessing.Process):
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
    b = multiprocessing.Array('i',8)
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
      f = g << abs(8-ax)
      e = ~f & mask
      b[ay] = e
      self.p = multiprocessing.Process(name='myname', target = self.display(ay, b), args = (ay, b))
      self.p.daemon = True
      self.p.start()
      time.sleep(0.1)
  def display(self, num, c):
    self.shifter.shiftByte(c[num])
    self.shifter.shiftByte(1 << (num))
