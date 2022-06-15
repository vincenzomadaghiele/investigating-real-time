RUN ON RASPBERRY:
python sensor.py --pin 7 &
python sensor.py --pin 11 &
python sensor.py --pin 13 &
python sensor.py --pin 15 &
python sensor.py --pin 16 &
python sensor.py --pin 18 &
python server.py &

RUN ON PC: 
python osc_adaptor.py &
python grid_split_server.py &
pure data receive_data.pd