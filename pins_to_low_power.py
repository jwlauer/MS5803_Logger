'''
Function for minimizing power use by pins while sleeping
Modified from lowpower.py at
https://gist.github.com/dpgeorge/bf477eb883b6d189eae9

'''
import pyb
from pyb import Pin




rtc = pyb.RTC()

def reset_pins():
    if hasattr(Pin.board, 'X1'):
        # pyboard
        pins = [
            (Pin.board.X1,  Pin.PULL_UP),
            (Pin.board.X2,  Pin.PULL_UP),
            (Pin.board.X3,  Pin.PULL_UP),
            (Pin.board.X4,  Pin.PULL_UP),
            (Pin.board.X5,  Pin.PULL_UP),
            (Pin.board.X6,  Pin.PULL_UP),
            (Pin.board.X7,  Pin.PULL_UP),
            (Pin.board.X8,  Pin.PULL_UP),
            (Pin.board.X9,  Pin.PULL_NONE), # I2C SCL
            (Pin.board.X10, Pin.PULL_NONE), # I2C SDA
            (Pin.board.X11, Pin.PULL_UP),
            (Pin.board.X12, Pin.PULL_UP),

            (Pin.board.Y1,  Pin.PULL_UP),
            (Pin.board.Y2,  Pin.PULL_UP),
            (Pin.board.Y3,  Pin.PULL_UP),
            (Pin.board.Y4,  Pin.PULL_UP),
            (Pin.board.Y5,  Pin.PULL_UP),
            (Pin.board.Y6,  Pin.PULL_UP),
            (Pin.board.Y7,  Pin.PULL_UP),
            (Pin.board.Y8,  Pin.PULL_UP),
            (Pin.board.Y9,  Pin.PULL_NONE), # I2C SCL
            (Pin.board.Y10, Pin.PULL_NONE), # I2C SDA
            (Pin.board.Y11, Pin.PULL_UP),
            (Pin.board.Y12, Pin.PULL_UP),

            #(Pin.board.X17, Pin.PULL_NONE), # USR SW already configured
            (Pin.board.X18, Pin.PULL_UP),
            (Pin.board.X19, Pin.PULL_UP),
            (Pin.board.X20, Pin.PULL_UP),
            (Pin.board.X21, Pin.PULL_UP),
            (Pin.board.X22, Pin.PULL_UP),
        ]

    if hasattr(Pin.board, 'MMA_AVDD'):
        pins += [
            (Pin.board.MMA_AVDD,    Pin.PULL_DOWN),
            (Pin.board.MMA_INT,     Pin.PULL_NONE), # BOOT1 pulled low by 100k
        ]

    if hasattr(Pin.board, 'SD_D0'):
        pins += [
            (Pin.board.SD_D0,       Pin.PULL_UP),
            (Pin.board.SD_D1,       Pin.PULL_UP),
            (Pin.board.SD_D2,       Pin.PULL_UP),
            (Pin.board.SD_D3,       Pin.PULL_UP),
            (Pin.board.SD_CMD,      Pin.PULL_UP),
            (Pin.board.SD_CK,       Pin.PULL_UP),
            #(Pin.board.SD_SW,       Pin.PULL_NONE), # already configured
        ]

    if hasattr(Pin.board, 'USB_VBUS'):
        pins += [
            (Pin.board.USB_VBUS,    Pin.PULL_UP),
            (Pin.board.USB_DM,      Pin.PULL_UP),
            (Pin.board.USB_DP,      Pin.PULL_UP),
        ]
        if hasattr(Pin.board, 'USB_ID'):
            pins += [(Pin.board.USB_ID, Pin.PULL_UP)]

    # configure pins as input to reduce current leakage
    for pin, pull in pins:
        pin.init(Pin.IN, pull)
