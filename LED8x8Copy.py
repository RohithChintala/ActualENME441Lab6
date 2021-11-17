import time
from shifter import Shifter    # extend by composition
import multiprocessing

class LED8x8Copy(multiprocessing.Process):
  def __init__(self, data, latch, clock, num, a):
    #self.shifter = Shifter(data, latch, clock)
    #multiprocessing.Process.__init__(self, target=self.display)
    while True:
      self.b = multiprocessing.Array('i',8)
      self.b[num] = a[num]
      self.shifter = Shifter(data, latch, clock)
      #self.b = multiprocessing.Array('i',8)
      #self.b[num] = a[num]
      self.p = multiprocessing.Process(target = self.display, args = (num,))
      self.p.daemon = True
      self.p.start()
      self.p.join()
  def display(self, num):
    self.shifter.shiftByte(self.b[num])
    self.shifter.shiftByte(1 << (num))
