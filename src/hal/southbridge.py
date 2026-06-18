# src/hal/southbridge.py

from machine import I2C, Pin


# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

SB_ADDR = 0x1F

SB_SDA = 6
SB_SCL = 7

SB_BAUDRATE = 10_000


# Registers

SB_REG_KEY = 0x04
SB_REG_BKL = 0x05
SB_REG_RST = 0x08
SB_REG_FIF = 0x09
SB_REG_BK2 = 0x0A
SB_REG_BAT = 0x0B
SB_REG_OFF = 0x0E

SB_WRITE = 0x80


_i2c = None


# ------------------------------------------------------------------
# Initialization
# ------------------------------------------------------------------

def init():
    global _i2c

    if _i2c is None:

        _i2c = I2C(
            1,
            scl=Pin(SB_SCL),
            sda=Pin(SB_SDA),
            freq=SB_BAUDRATE
        )


def deinit():
    global _i2c

    if _i2c:

        _i2c.deinit()

        _i2c = None


# ------------------------------------------------------------------
# Internal helpers
# ------------------------------------------------------------------

def _ensure_init():

    if _i2c is None:

        init()


def _read_register(register):

    _ensure_init()

    try:

        _i2c.writeto(SB_ADDR, bytes([register]))

        data = _i2c.readfrom(SB_ADDR, 2)

        return data[1]

    except OSError:

        return None


def _write_register(register, value):

    _ensure_init()

    try:

        _i2c.writeto(
            SB_ADDR,
            bytes([register | SB_WRITE, value])
        )

        data = _i2c.readfrom(SB_ADDR, 2)

        return data[1]

    except OSError:

        return None


# ------------------------------------------------------------------
# Keyboard
# ------------------------------------------------------------------

def read_keyboard():

    _ensure_init()

    try:

        _i2c.writeto(SB_ADDR, bytes([SB_REG_FIF]))

        data = _i2c.readfrom(SB_ADDR, 2)

        return (data[0] << 8) | data[1]

    except OSError:

        return 0


def read_keyboard_state():

    _ensure_init()

    try:

        _i2c.writeto(SB_ADDR, bytes([SB_REG_KEY]))

        data = _i2c.readfrom(SB_ADDR, 2)

        return data[0]

    except OSError:

        return 0


# ------------------------------------------------------------------
# Battery
# ------------------------------------------------------------------

def read_battery():

    return _read_register(SB_REG_BAT)


# ------------------------------------------------------------------
# LCD backlight
# ------------------------------------------------------------------

def read_lcd_backlight():

    return _read_register(SB_REG_BKL)


def write_lcd_backlight(level):

    level = max(0, min(255, level))

    return _write_register(
        SB_REG_BKL,
        level
    )


# ------------------------------------------------------------------
# Keyboard backlight
# ------------------------------------------------------------------

def read_keyboard_backlight():

    return _read_register(SB_REG_BK2)


def write_keyboard_backlight(level):

    level = max(0, min(255, level))

    return _write_register(
        SB_REG_BK2,
        level
    )


# ------------------------------------------------------------------
# Power
# ------------------------------------------------------------------

def power_off_supported():

    value = _read_register(SB_REG_OFF)

    if value is None:

        return False

    return value > 0


def power_off(delay=2):

    delay = max(0, min(255, delay))

    return _write_register(
        SB_REG_OFF,
        delay
    )


def reset(delay=2):

    delay = max(0, min(255, delay))

    return _write_register(
        SB_REG_RST,
        delay
    )