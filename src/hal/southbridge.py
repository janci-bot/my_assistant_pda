from machine import I2C, Pin

SB_ADDR = 0x1F

i2c = I2C(
    1,
    scl=Pin(7),
    sda=Pin(6),
    freq=10000
)

def read_battery():
    pass

def read_lcd_backlight():
    pass

def write_lcd_backlight(level):
    pass

def read_keyboard_backlight():
    pass

def write_keyboard_backlight(level):
    pass

def power_off(delay):
    pass

def reset(delay):
    pass