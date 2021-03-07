# rpi-pan-tilt

Functions for moving servos in a pan-tilt way. \
This project makes use of the [_pigpio_](http://abyz.me.uk/rpi/pigpio/index.html) library wich uses hardware PWM and cares about timing. \
Using software PWM the servos are not accurate enough, also they have interference (jittering/glitching) and, in some cases, the move in really unexpected ways. \
Just for referece, it's also the [ServoBlaster](https://github.com/BioMachinesLab/drones/wiki/Installing-Servoblaster) library which is made particularly for servo handling. But I prefer pigpio which is easier and it's also for general purpose.

## Requirements
Install [pigpio](http://abyz.me.uk/rpi/pigpio/download.html)
Install [python3-pigpio](http://abyz.me.uk/rpi/pigpio/download.html)

Then start pigpiod
```bash
sudo pgpiod
```