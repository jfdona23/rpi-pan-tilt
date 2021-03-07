# rpi-pan-tilt

Functions for moving servos in a pan-tilt way. \
This project makes use of the [__pigpio__](http://abyz.me.uk/rpi/pigpio/index.html) library wich uses hardware PWM and cares about timing. \
Using software PWM the servos are not accurate enough, also they have interference (jittering/glitching) and, in some cases, the move in really unexpected ways. \
Just for referece, it's also the [__ServoBlaster__](https://github.com/BioMachinesLab/drones/wiki/Installing-Servoblaster) library which is made particularly for servo handling. But I prefer pigpio which is easier and it's also for general purpose.

## Requirements
* Install __pigpio__ and __python3-pigpio__ (Raspbian and derivatives)
* General install instructions [here](http://abyz.me.uk/rpi/pigpio/download.html)

* Then start pigpiod
    ```bash
    sudo pgpiod
    ```