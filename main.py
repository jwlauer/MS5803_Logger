""" Module for executing code on embedded device

This module runs the logger program.  It flashes the blue led once, for one seccond, if there is an error, then
goes into standby and will try again after the appropriate logging interval.

"""

import pyb,time
#pyb.freq(36000000)
log_interval = 30 #seconds
try:
    import logger_pres_temp
    logger_pres_temp.log(log_interval)
except:
    pyb.led(4).on()
    time.sleep(1)
    pyb.RTC.wakeup(log_interval*1000)
    pyb.standby()