from adafruit_circuitplayground.express import cpx 
import time
import random 

colors = [(255, 0, 255), (0, 100, 0),(0, 0, 139)]

while True:
  if cpx.switch == True:
    if cpx.button_a:
        while True:
          for indice in range(0,10):
            cpx.pixels[indice] = (random.choice(colors))
            time.sleep(0.1)
            cpx.pixels.fill((0,0,0))
            time.sleep(0.10)
    if cpx.button_b:
      cpx.pixels.fill((255, 0, 0))
  else:
    cpx.pixels.fill((0,0,0))
