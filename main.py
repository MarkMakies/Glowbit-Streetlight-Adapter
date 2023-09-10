from machine import Pin
import neopixel

numPixels = 64
NeoPin = Pin(14,Pin.OUT)                    
Neo = neopixel.NeoPixel(NeoPin,numPixels)

def Flood(r,g,b):
   for k in range(numPixels):
       Neo[k] = ((r, g, b))    
   neopixel.NeoPixel.write(Neo)

Flood(255,139,21)   # iPhone measure 3250 K on grey card reflection
