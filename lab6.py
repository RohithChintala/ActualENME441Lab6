import time
from LED8x8 import LED8x8
import multiprocessing
import random

dataPin, latchPin, clockPin = 13, 19, 26
LED = LED8x8(dataPin, latchPin, clockPin)
