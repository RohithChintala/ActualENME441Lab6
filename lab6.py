from LED8x8 import LED8x8
import multiprocessing


dataPin, latchPin, clockPin = 13, 19, 26
LED = LED8x8(dataPin, latchPin, clockPin) #initializes LED as a LED8x8 class to run init code
