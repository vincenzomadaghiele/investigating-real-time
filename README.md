# Investigating real-time feedback of energy consumption and emission data through sonic interaction design

This repository contains all the code for the paper ([bib](./investigating.bib)):

> Vincenzo Madaghiele, Sandra Pauletto.
> [**Investigating real-time feedback of energy consumption and emission data through sonic interaction design**](https://icad2022.icad.org/wp-content/uploads/2022/06/ICAD2022_20.pdf).
> In _Proceedings of 27th International Conference on Auditory Display (ICAD)_, June 24-27 2022, Online.


### Abstract:
As buildings become increasingly automated and energy efficient, the relative impact of occupants on the overall building carbon footprint is expected to increase. Research shows that by changing occupant behaviour energy savings between 5 and 15 % could be achieved. A commonly used device for energy-related behaviour change is the smart meter, a visual-based interface which provides users with data about energy consumption and emissions of their household.
This paper approaches the problem from a Sonic Interaction Design point of view, with the aim of developing an alternative, sound-based design to provide feedback about some of the data usually accessed through smart meters. In this work, we experimented with sonic augmentation of a common household object, a door mat, in order to provide a non-intrusive everyday sonic interaction. The prototype that we built is an energy-aware sonic carpet that provides real-time feedback on home electricity consumption and emissions through sound. An experiment has been designed to evaluate the prototype from a user experience perspective, and to assess how users understand the chosen sonifications.


## Instructions
Run on RaspberryPi:
```
$ python sensor.py --pin 7 &
python sensor.py --pin 11 &
python sensor.py --pin 13 &
python sensor.py --pin 15 &
python sensor.py --pin 16 &
python sensor.py --pin 18 &
python server.py &
```
Run on Pc:
```
$ python osc_adaptor.py &
python grid_split_server.py &
pure data receive_data.pd
```
