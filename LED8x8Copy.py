import time
from shifter import Shifter    # extend by composition
import multiprocessing

class LED8x8Copy(multiprocessing.Process):
  def __init__(self, data, latch, clock, num, a):
    self.shifter = Shifter(data, latch, clock)
    self.b = multiprocessing.Array('i',8)
    self.b[num] = a[num]
    multiprocessing.Process.__init__(self, target=self.display(num,a), args= (num, a))
    #self.p = multiprocessing.Process(name='myname', target = self.display(num, a), args = (num, a))
    #self.p.daemon = True
    #self.p.start()
    #self.p.join()
    #while True:
      #self.display(num, a)
      #self.b = multiprocessing.Array('i',8)
      #self.b[num] = a[num]
      #self.p = multiprocessing.Process(name='myname', target = self.display(num, a), args = (num, a))
      #self.p.daemon = True
      #self.p.join()
  def display(self, num, a):
    while True:
      self.shifter.shiftByte(self.b[num])
      self.shifter.shiftByte(1 << (num))
