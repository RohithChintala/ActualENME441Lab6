import time
from shifter import Shifter    # extend by composition
import multiprocessing

class LED8x8Copy(multiprocessing.Process):
  def __init__(self, data, latch, clock, num, b):
    #self.shifter = Shifter(data, latch, clock)
    #multiprocessing.Process.__init__(self, target=self.display)
    self.b = multiprocessing.Array('i',8)
    while True:
      self.b = b
      self.shifter = Shifter(data, latch, clock)
      #self.b = multiprocessing.Array('i',8)
      #self.b[num] = a[num]
      self.p = multiprocessing.Process(target = self.display, args = (num,))
      self.p.daemon = True
      #self.p.start()
      #self.p.join()
      time.sleep(0.00001)
  def display(self, num):
    self.shifter.shiftByte(self.b[num])
    self.shifter.shiftByte(1 << (num))
