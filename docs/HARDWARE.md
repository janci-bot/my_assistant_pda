# PicoCalc Hardware Map

Last updated: 2026-07

---

# CPU

MCU: Raspberry Pi Pico 2 W

SoC: RP2350

Clock: 230 MHz

RAM: 520 KB SRAM

Wireless:
- WiFi
- Bluetooth

---

# LCD

Display controller: ST7789

Resolution: 320x320 px

Frame buffer: 320x480 px

Interface:
SPI1

GPIO10  SCK
GPIO11  MOSI
GPIO12  MISO
GPIO13  CS
GPIO14  DC
GPIO15  RST

Known facts

- FrameBuffer available through `lcd.fb`
- Supported primitives:
  - pixel()
  - line()
  - rect()
  - fill_rect()
  - fill()
  - text()
  - ellipse()
  - poly()
  - scroll()
  - blit()
  - hline()
  - vline()

Display size confirmed:

320x320

---

# LCD Colors

Driver does not use standard RGB565 mapping.

Experimentally confirmed mapping:

Requested     Visible

0x0000        Black
0xFFFF        White
0xF800        Blue
0x07E0        Red
0x001F        Green
0x07FF        Yellow

This mapping should be used by all custom drawing code.

---

# Southbridge

Controller address:

0x1F

Interface:

I2C1

GPIO6  SDA
GPIO7  SCL

---

# Southbridge Registers

0x04  KEY
0x05  LCD_BACKLIGHT
0x08  RESET
0x09  KEY_FIFO
0x0A  KEYBOARD_BACKLIGHT
0x0B  BATTERY
0x0E  POWER_OFF

---

# Keyboard

Confirmed key codes

BACK   = 8
ENTER  = 10
SHIFT  = 162
ESC    = 177
LEFT   = 180
UP     = 181
DOWN   = 182
RIGHT  = 183

Keyboard controller uses FIFO register (0x09).

---

# Audio

Stereo output

LEFT  = GPIO26

RIGHT = GPIO27

Verified:

✓ PWM output works directly from MicroPython

Example:

PWM(Pin(26))

Picoware audio module exists but is intentionally NOT used.

---

# Battery

Battery percentage available from

Southbridge register:

0x0B

Already successfully tested.

---

# Backlight

LCD backlight register:

0x05

Keyboard backlight register:

0x0A

---

# Power

Power OFF register:

0x0E

Reset register:

0x08

---

# Project Rules

MY_ASSISTANT does not depend on Picoware.

Allowed:

- MicroPython
- machine
- framebuf
- own drivers

Not allowed:

- Picoware GUI
- Picoware Audio
- Picoware Applications

Only hardware knowledge discovered from Picoware source code may be reused.

---

# Current MY_ASSISTANT UI

Resolution:

320x320

Current screens

BOOT

↓

Welcome Ritual

↓

Password

↓

HOME

Navigation

UP/DOWN
Move inside menu

LEFT/RIGHT
Reserved

ENTER
Open item

ESC
Back

Navigation indicator

◀ 1/1 ▶

◀ 2/3 ▶

◀ 3/3 ▶

---

# HOME Menu v0.1

Poznamky
    Nova
    Zoznam
    Secret

Kalendar
    Den
    Tyzden
    Mesiac
    Rok
    Najblizsia udalost
    Sviatky
    Narodeniny/Meniny

TODO
    Aktivne
    Dokoncene

Kontakty
    Novy
    Zoznam
    Oblubene

Nastavenia
    Displej
    Zvuk
    WiFi
    Bluetooth
    Cas a datum
    Informacie

Aplikacie
    Tankovanie
    Motorka
    GPS
