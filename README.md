# rpi-pan-tilt

Functions for moving servos in a pan-tilt way. \
This project makes use of the [__pigpio__](http://abyz.me.uk/rpi/pigpio/index.html) library wich uses hardware PWM and cares about timing. \
Using software PWM the servos are not accurate enough, also they have interference (jittering/glitching) and, in some cases, the move in really unexpected ways. \
Just for referece, it's also the [__ServoBlaster__](https://github.com/BioMachinesLab/drones/wiki/Installing-Servoblaster) library which is made particularly for servo handling. But I prefer pigpio which is easier and it's also for general purpose.

## Requirements
* Install __pigpio__ and __python3-pigpio__ (Raspbian and derivatives)
* General install instructions [here](http://abyz.me.uk/rpi/pigpio/download.html)

* Then enable pigpio at boot time and start it
    ```bash
    sudo systemctl enable pigpiod
    sudo systemctl start pigpiod
    ```
* Check the daemon status
    ```bash
    sudo systemctl status pigpiod
    ```

## Issues
* Pigpio versions under 73 could have an issue where the daemon starts listening to an IPv6 socket only. Therefore, some clients are not able to connect since mostly use localhost on IPv4. If you face this issue the workaround is to edit the Systemd Unit file
    ```bash
    # Edit the unit file as root
    /etc/systemd/system/multi-user.target.wants/pigpiod.service

    # Edit the ExecStart line as follows:
    ExecStart=/usr/bin/pigpiod -l -n 127.0.0.1

    # Reload Units
    sudo systemctl daemon-reload

    # Restart the service (o the entire host)
    sudo systemctl restart pigpiod
    ```
* If you're running a 64 bits OS you will need to compile pigpio by yourself. Follow the [generall install instructions](http://abyz.me.uk/rpi/pigpio/download.html)