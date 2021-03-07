"""
Controlling two servos mounted inside a Pan-Tilt support
"""
from time import sleep

import pigpio


# ----------------------------------------------------------------------------------------------- #
# General Config
# ----------------------------------------------------------------------------------------------- #
pan_servo = 18 # Pin12
tilt_servo = 27 # Pin13

pi = pigpio.pi()

# ----------------------------------------------------------------------------------------------- #
# Servo Config
# ----------------------------------------------------------------------------------------------- #
low_pulse = 500  # 0 degrees
neutral_pulse = 1500  # 90 degrees
high_pulse = 2500  # 180 degrees
step = (high_pulse - low_pulse) / 180 # How many microseconds are needed for moving one degree

# ----------------------------------------------------------------------------------------------- #
# Main Program
# ----------------------------------------------------------------------------------------------- #
def get_angle(servo):
    """Get current angle
    
    Args:
        - servo (int): GPIO where the servo is connected
    
    Returns:
        - angle (int): Current angle
    """

    return (pi.get_servo_pulsewidth(servo) - low_pulse) / step

def set_angle(servo_list, angle):
    """Set servo angle
    It translates servo angle into a PWM duty cycle. This is because servos usually
    respond to pulses from 1000us to 2000us (SG90 could be more from 500us to 2500us).
    In this way if we use a PWM set to 50hz we will have a duty cycle of 20000us,
    therefore our pulses will be comprehended between a duty cycle from 2.5% to 12.5%
    
        ```
        500  / 20000 = 0.025 or  2.5 % dutycycle
        1000 / 20000 = 0.05  or  5.0 % dutycycle
        1500 / 20000 = 0.075 or  7.5 % dutycycle
        2000 / 20000 = 0.1   or 10.0 % dutycycle
        2500 / 20000 = 0.125 or 12.5 % dutycycle
        ```
    
    Args:
        - servo_list (list): GPIO where the servo(s) is/are connected.
            If there is only one servo connected, it could be passed as an integer
        - angle (int): Angle to set the servo
    """

    if not isinstance(servo_list, list):
        servo_list = list([servo_list])
    for servo in servo_list:
        pulse_width = (angle * step) + low_pulse
        pi.set_servo_pulsewidth(servo, pulse_width)

def set_angle_smooth(servo_list, angle, step=1, delay=0.05):
    """Set an angle smoothly by traversing several angles until reaching the desired one
    
    Args:
        - servo_list (list): GPIO where the servo(s) is/are connected.
            If there is only one servo connected, it could be passed as an integer
        - angle (int): Angle to set the servo
        - step (int): Step in degrees from angle to angle
        - delay (float): Time in seconds to wait between angles
    """

    step_bkp = step
    if not isinstance(servo_list, list):
        servo_list = list([servo_list])
    for servo in servo_list:
        current_angle = int(get_angle(servo))
        if current_angle > angle:
            step = -step
        for a in range(current_angle, angle+step, step):
            print(a)
            set_angle(servo, a)
            sleep(delay)
        step = step_bkp


if __name__ == "__main__":
    servos = [pan_servo, tilt_servo]
    set_angle(servos, 90)
    set_angle_smooth(servos, 180)
    set_angle_smooth(servos, 0)
    set_angle(servos, 90)
    sleep(0.25)
