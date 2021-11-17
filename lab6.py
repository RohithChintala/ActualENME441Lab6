import time
from LED8x8 import LED8x8
from LED8x8Copy import LED8x8Copy
import multiprocessing
import random

dataPin, latchPin, clockPin = 13, 19, 26
LED = LED8x8Copy(dataPin, latchPin, clockPin)
