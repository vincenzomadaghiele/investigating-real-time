'''
This is an OSC adaptor
----------------------------
it gets data from sensors and current 
electricity consumption and grid split
from REST APIs, perform analysis
and send everything to pd through OSC
'''

import json
import requests
import time
from pythonosc import udp_client
from datetime import datetime


if __name__ == '__main__':

    # OSC CLIENT AND PORT
    ip_local_osc = "127.0.0.1"
    port_osc = 5010
    client = udp_client.SimpleUDPClient(ip_local_osc, port_osc)
    sensor_pins = [7, 11, 13, 15, 16, 18]

    while True:

        # GET SENSOR DATA
        '''
        try:
            ip_rasp = '192.168.43.248' 
            port_sensor = '8080'
            for pin in sensor_pins:
                uri = f'http://{ip_rasp}:{port_sensor}/{pin}'
                r = requests.get(uri)
                result = r.json()
                #print(result)

                # check for timing
                now = time.time()
                if now - result['last_update'] < 1:
                    # send through OSC
                    client.send_message("/sensor/"+str(result["sensor_pin"]), result["value"])
                    print("/sensor/"+str(result["sensor_pin"]) + ' : ' + str(result["value"]))
                else:
                    # send really high value to turn off
                    client.send_message("/sensor/"+str(result["sensor_pin"]), 1e5)
                    print("/sensor/"+str(result["sensor_pin"]) + ' : ' + str(1e5))

        except:
            print('Could not get sensor data')
        '''
        # perform gesture recognition on data
        # send output to pd trough OSC

        try:

            # GET ENERGY DATA
            port_split = 50000
            cmd = 'all' # could change
            uri = f'http://{ip_local_osc}:{port_split}/{cmd}'
            r = requests.get(uri)
            result = r.json()
            # print(result)

            # send grid split
            split = result['value']
            msg = str(split[1])+' '+str(split[2])+' '+str(split[3])+' '+str(split[4])+' '+str(split[5])+' '+str(split[6])
            client.send_message("/gridSplit", msg)
            print("/gridSplit" + ' : ' + msg)

            # send total consumption
            msg = str(split[0])
            client.send_message("/tot_cons", msg)
            print("/tot_cons" + ' : ' + msg)


            # GET EMISSIONS
            cmd = 'emissions' # could change
            uri = f'http://{ip_local_osc}:{port_split}/{cmd}'
            r = requests.get(uri)
            result = r.json()
            # print(result)

            msg = str(result['value'])
            client.send_message("/emissions", msg)
            print("/emissions" + ' : ' + msg)


            # GET CUMULATIVE CONSUMPTION
            cmd = 'cumulative_consumption' # could change
            uri = f'http://{ip_local_osc}:{port_split}/{cmd}'
            r = requests.get(uri)
            result = r.json()
            # print(result)

            msg = str(result['value'])
            client.send_message("/cumulative_consumption", msg)
            print("/cumulative_consumption" + ' : ' + msg)


            # GET CUMULATIVE EMISSIONS
            cmd = 'cumulative_emissions' # could change
            uri = f'http://{ip_local_osc}:{port_split}/{cmd}'
            r = requests.get(uri)
            result = r.json()
            # print(result)

            msg = str(result['value'])
            client.send_message("/cumulative_emissions", msg)
            print("/cumulative_emissions" + ' : ' + msg)

        except:
            print('Could not get energy data')

        time.sleep(0.0001)
