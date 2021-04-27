import smbus
import time

DEVICE = 0x23 # I2C address of sensor
bus = smbus.SMBus(1)

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number. Optional parameter 'decimals'
  # will round to specified number of decimal places.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):
  # Read data from I2C interface
  data = bus.read_i2c_block_data(addr,DEVICE)
  return convertToNumber(data)

try:
    while 1:
        lightLevel=readLight()
        print(lightLevel)
        if(lightLevel > 500):
            print("Too bright")
        elif(lightLevel > 200 and lightLevel <= 500):
            print("bright")
        elif(lightLevel > 100 and lightLevel <= 200):
            print("Medium")
        elif(lightLevel > 20 and lightLevel <= 100):
            print("dark")
        elif(lightLevel <= 20):
            print("Too dark")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopped")
