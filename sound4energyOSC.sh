#!/usr/bin/env bash

echo "Starting up the sound4energy code on Raspberry!"
cd Sound4energy
python sensorOSC.py --pin 7 &
python sensorOSC.py --pin 11 &
python sensorOSC.py --pin 13 &
python sensorOSC.py --pin 15 &
python sensorOSC.py --pin 16 &
python sensorOSC.py --pin 18 &