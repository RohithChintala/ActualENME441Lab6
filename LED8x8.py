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
        if ax >= 0: #checks that ax is within the led screen
          if ax <= 7: 
            if ay >= 0:
              if ay <= 7:
                h = 1 #if final movement is within leds then exits while loop
        else:
          h = 0 #if movement is outside of leds then while loop continues
          ax -= x #resests ax to original value
          ay -= y #resets ay to original value
      f = g << abs(8-ax) #sets f to be binary value with the ax bit being 1
      e = ~f & mask #inverses the values of binary f
      a[ay] = e #sets multiprocessing array for row ay to equal e
      self.p = multiprocessing.Process(name='myname', target = self.display(ay, a), args = (ay, a)) #defines multiprocessing process
      self.p.daemon = True #sets daemon true for multiprocessing process
      self.p.start() #starts multiprocessing process
      time.sleep(0.1) #sleeps for .1 seconds
  def display(self, num, c):
    self.shifter.shiftByte(c[num])
    self.shifter.shiftByte(1 << (num))
