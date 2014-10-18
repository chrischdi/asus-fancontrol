#!/usr/bin/env python3

import re
import subprocess
import time

conf = {}
conf['update_interval'] = 10
conf['speed'] = [(50, '1'),
                 (60, '72'),
                 (65, '88'),
                 (70, '104'),
                 (75, '128'),
                 (80, 'auto')]
conf['executable'] = '/usr/bin/fanctrl'
regex = re.compile('\+(\d\d)\.\d')


def get_current_temperature():
    sensors = subprocess.check_output(['/usr/bin/sensors'])
    match = regex.search(sensors.decode())
    return int(match.group(1))


def set_speed(speed):
    subprocess.call(['/usr/bin/fanctrl', speed])


def main():
    last_temp = 100
    last_speed = ''
    while True:
        temp = get_current_temperature()
        for k in conf['speed']:
            if k[0] <= temp:
                # always increase fan speed immediately but only lower it if
                # the temp has decreased by 3
                if (temp < last_temp-2) or temp >= last_temp:
                    new_speed = k[1]
                    last_temp = k[0]
        print('Temp: {}, Speed: {}'.format(temp, new_speed))
        if last_speed != new_speed:
            set_speed(new_speed)
            last_speed = new_speed
        time.sleep(conf['update_interval'])

if __name__ == '__main__':
    main()
