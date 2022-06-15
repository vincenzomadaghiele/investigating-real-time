import RPi.GPIO as GPIO
import json
import time
import socket
import argparse
import glob
from pythonosc import udp_client


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

    #ip_local_osc = "127.0.0.1"
    ip_local_osc = "192.168.43.226"
    port_osc = 5010
    client = udp_client.SimpleUDPClient(ip_local_osc, port_osc)

    pin_to_circuit = args.pin
    try:
        while True:
            value, ts = rc_time(pin_to_circuit)
            print(value)            
            # send through OSC
            client.send_message("/sensor/" + str(pin_to_circuit), value)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

