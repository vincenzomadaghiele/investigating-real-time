import RPi.GPIO as GPIO
import json
import time
import socket
import argparse
import glob

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)

def rc_time (pin):

    count = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.01)
    GPIO.setup(pin, GPIO.IN)
    while (GPIO.input(pin) == GPIO.LOW):
        count += 1
    ts = time.time()

    return count, ts

if __name__ == "__main__":

    # params
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", type=int, default=7,
      help="Pin on Raspberry to listen to")
    args = parser.parse_args()

    pin_to_circuit = args.pin
    try:
        while True:
            value, ts = rc_time(pin_to_circuit)
            print(value)

            # temporary solution
            source_path = 'sensors/*.json'
            sensors = glob.glob(source_path)

            # open catalog
            for path in sensors:
                try:
                    f = open(path)
                    sensor = json.load(f)
                    f.close()
                    if sensor['sensor_pin'] == pin_to_circuit:
                        sensor['value'] = value
                        sensor['last_update'] = ts

                        # save catalog
                        with open(path, 'w') as f:
                            json.dump(sensor, f)
                except:
                    print('Could not access values')

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

