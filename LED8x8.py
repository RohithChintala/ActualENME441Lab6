import time
from shifter import Shifter    # extend by composition
import multiprocessing

class LED8x8(multiprocessing.Process):
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
    multiprocessing.Process.__init__(self)
  def display(self, num, a):
    self.shifter.shiftByte(a[num])
    self.shifter.shiftByte(1 << (num))

