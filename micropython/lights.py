import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(13), 5)

# valid values are 0 to 254

np[0] = (5, 0, 0) # set to red
np[1] = (0, 0, 5) # set to green
np[2] = (0, 5, 0)  # set to blue
np[3] = (5, 0, 5)  # set to purple
np[4] = (0, 0, 5)  # set to blue

np.write()
