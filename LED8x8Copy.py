import time
from shifter import Shifter    # extend by composition
import multiprocessing

class LED8x8Copy(multiprocessing.Process):
  def __init__(self, data, latch, clock, num, a):
    self.shifter = Shifter(data, latch, clock)
    #multiprocessing.Process.__init__(self, target=self.display)
    while True:
      b = multiprocessing.Array('i',8)
      b[num] = a[num]
      self.p = multiprocessing.Process(target = self.display, args = (num, self.b))
      self.p.daemon = True
      self.p.start()
      time.sleep(0.1)
  def display(self, num, b):
    self.shifter.shiftByte(b[num])
    self.shifter.shiftByte(1 << (num))
