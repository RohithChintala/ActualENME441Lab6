import time
import random
ay = 5
ax = 5
g = 0b1
mask = 0b11111111
dataPin, latchPin, clockPin = 13, 19, 26
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
  #a = multiprocessing.Array('i',8)
  a = [0,0,0,0,0,0,0,0]
  a[ay] = e
  print(a[ay])
  time.sleep(1)
