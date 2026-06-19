# lab.py

from machine import I2C, Pin
import time


# --------------------------------------------------
# Southbridge
# --------------------------------------------------

SB_ADDR = 0x1F

SB_REG_BKL = 0x05
SB_REG_RST = 0x08
SB_REG_FIF = 0x09
SB_REG_BK2 = 0x0A
SB_REG_BAT = 0x0B
SB_REG_OFF = 0x0E

SB_WRITE = 0x80


i2c = I2C(
    1,
    scl=Pin(7),
    sda=Pin(6),
    freq=10000
)


# --------------------------------------------------
# Helpers
# --------------------------------------------------

def read_register(register):

    i2c.writeto(
        SB_ADDR,
        bytes([register])
    )

    data = i2c.readfrom(
        SB_ADDR,
        2
    )

    return data


def write_register(register, value):

    i2c.writeto(
        SB_ADDR,
        bytes([
            register | SB_WRITE,
            value
        ])
    )


# --------------------------------------------------
# Tests
# --------------------------------------------------

def battery_test():

    data = read_register(SB_REG_BAT)

    print()

    print("Battery:", data[1], "%")


def lcd_backlight_test():

    print()

    for level in [20, 80, 150, 255]:

        print("LCD:", level)

        write_register(
            SB_REG_BKL,
            level
        )

        time.sleep(1)


def keyboard_backlight_test():

    print()

    for level in [0, 50, 100, 255]:

        print("Keyboard:", level)

        write_register(
            SB_REG_BK2,
            level
        )

        time.sleep(1)


def keyboard_test():

    print()

    print("Press keys...")

    print("Ctrl+C to stop")

    print()

    while True:

        i2c.writeto(
            SB_ADDR,
            bytes([SB_REG_FIF])
        )

        data = i2c.readfrom(
            SB_ADDR,
            2
        )

        value = (data[0] << 8) | data[1]

        if value:

            print(
                "state:",
                data[0],
                "key:",
                data[1]
            )

        time.sleep_ms(50)


def reset_test():

    print()

    print("Reset in 2 seconds")

    time.sleep(2)

    write_register(
        SB_REG_RST,
        2
    )


def power_off_test():

    print()

    print("Power off in 2 seconds")

    time.sleep(2)

    write_register(
        SB_REG_OFF,
        2
    )


# --------------------------------------------------
# Menu
# --------------------------------------------------

while True:

    print()

    print("=== MY_ASSISTANT PDA LAB ===")

    print()

    print("1 - Battery")

    print("2 - LCD Backlight")

    print("3 - Keyboard Backlight")

    print("4 - Keyboard")

    print("5 - Reset")

    print("6 - Power Off")

    print("q - Exit")

    print()

    choice = input("> ").lower()


    if choice == "1":

        battery_test()


    elif choice == "2":

        lcd_backlight_test()


    elif choice == "3":

        keyboard_backlight_test()


    elif choice == "4":

        keyboard_test()


    elif choice == "5":

        reset_test()


    elif choice == "6":

        power_off_test()


    elif choice == "q":

        break