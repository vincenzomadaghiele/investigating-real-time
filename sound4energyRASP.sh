#!/usr/bin/env bash

echo "Starting up the sound4energy code on Raspberry!"
cd Sound4energy
python sensor.py --pin 7 &
python sensor.py --pin 11 &
python sensor.py --pin 13 &
python sensor.py --pin 15 &
python sensor.py --pin 16 &
python sensor.py --pin 18 &
python server.py &
