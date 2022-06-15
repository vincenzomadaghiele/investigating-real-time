#!/usr/bin/env bash

echo "Starting up the sound4energy code on PC!"
cd grid_split
python grid_split_server.py
cd ..
python osc_adaptor.py