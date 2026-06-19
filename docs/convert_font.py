import re

SOURCE = "font8x8_basic.h"
TARGET = "font8.py"


with open(SOURCE, encoding="utf-8") as f:
    text = f.read()


blocks = re.findall(
    r'\{\s*((?:0x[0-9A-Fa-f]{2}\s*,?\s*){8})\}',
    text
)


font = {}

for code in range(32, 127):

    values = blocks[code]

    values = re.findall(
        r'0x[0-9A-Fa-f]{2}',
        values
    )

    font[chr(code)] = values


with open(TARGET, "w", encoding="utf-8") as f:

    f.write("# font8.py\n\n")

    f.write("FONT = {\n\n")

    for char, values in font.items():

        escaped = repr(char)

        f.write(f"    {escaped}: [\n")

        for value in values:

            f.write(f"        {value},\n")

        f.write("    ],\n\n")

    f.write("}\n")


print("font8.py created")